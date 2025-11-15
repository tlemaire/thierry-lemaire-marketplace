import express, { Request, Response } from 'express';
import { ProviderFactory } from '../providers';
import { AnthropicAPICompatibility } from '../utils/anthropic-api';
import { ErrorHandler } from '../utils/errors';
import { config } from '../config';
import { Readable } from 'stream';

const router = express.Router();

// Combined messages endpoint (handles both streaming and non-streaming)
router.post('/messages', async (req: Request, res: Response) => {
  try {
    // Validate request
    const anthropicRequest = AnthropicAPICompatibility.validateRequest(req.body);

    // Extract provider and model name
    const providerName = AnthropicAPICompatibility.extractProviderFromModel(
      anthropicRequest.model,
      config.defaultProvider
    );
    const modelName = AnthropicAPICompatibility.extractModelName(anthropicRequest.model, providerName);

    // Validate provider
    if (!ProviderFactory.validateProvider(providerName)) {
      throw ErrorHandler.createProxyError(
        `Unsupported provider: ${providerName}. Supported providers: ${ProviderFactory.getSupportedProviders().join(', ')}`,
        400
      );
    }

    // Create provider and transform request
    const provider = ProviderFactory.createProvider(providerName);
    const providerRequest = {
      ...anthropicRequest,
      model: modelName
    };
    const transformedRequest = provider.transformRequest(providerRequest);

    // Check if streaming is requested
    if (anthropicRequest.stream) {
      return await handleStreamingRequest(req, res, provider, transformedRequest);
    } else {
      return await handleNonStreamingRequest(req, res, provider, transformedRequest);
    }
  } catch (error) {
    ErrorHandler.handleError(error, res);
  }
});

async function handleNonStreamingRequest(
  req: Request,
  res: Response,
  provider: any,
  transformedRequest: any
) {
  try {
    // Make request to provider
    const providerResponse = await provider.createRequest(transformedRequest);

    // Transform response back to Anthropic format
    const anthropicResponse = provider.transformResponse(providerResponse);

    // Send response with Anthropic headers
    res.set(AnthropicAPICompatibility.createResponseHeader());
    res.json(anthropicResponse);
  } catch (error) {
    ErrorHandler.handleError(error, res);
  }
}

async function handleStreamingRequest(
  req: Request,
  res: Response,
  provider: any,
  transformedRequest: any
) {
  try {
    // Set up streaming response
    res.set(AnthropicAPICompatibility.createStreamHeader());
    res.flushHeaders();

    // Generate message ID
    const messageId = `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

    // Send stream start
    res.write(AnthropicAPICompatibility.createStreamStart(messageId));
    res.write(AnthropicAPICompatibility.createContentBlockStart());

    // Create stream request to provider
    const stream = await provider.createStreamRequest(transformedRequest);

    // Handle stream data
    stream.on('data', (chunk: Buffer) => {
      const lines = chunk.toString().split('\n');

      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const data = line.slice(6);
            if (data === '[DONE]') {
              res.write(AnthropicAPICompatibility.createStreamStop());
              res.end();
              return;
            }

            const providerChunk = JSON.parse(data);
            const anthropicChunk = provider.transformStreamChunk(providerChunk);

            if (anthropicChunk) {
              res.write(AnthropicAPICompatibility.formatStreamChunk(anthropicChunk));
            }
          } catch (parseError) {
            console.error('Error parsing stream chunk:', parseError);
          }
        }
      }
    });

    // Handle stream end
    stream.on('end', () => {
      res.write(AnthropicAPICompatibility.createStreamStop());
      res.end();
    });

    // Handle stream errors
    stream.on('error', (error: Error) => {
      console.error('Stream error:', error);
      if (!res.headersSent) {
        ErrorHandler.handleError(error, res);
      } else {
        res.end();
      }
    });

  } catch (error) {
    ErrorHandler.handleError(error, res);
  }
}

export default router;