import { AnthropicRequest, AnthropicResponse, AnthropicStreamChunk } from '../types';

export class AnthropicAPICompatibility {
  static validateRequest(request: any): AnthropicRequest {
    if (!request.model) {
      throw new Error('Model is required');
    }
    if (!request.messages || !Array.isArray(request.messages)) {
      throw new Error('Messages array is required');
    }
    if (!request.max_tokens) {
      throw new Error('max_tokens is required');
    }

    return request as AnthropicRequest;
  }

  static createResponseHeader(): Record<string, string> {
    return {
      'Content-Type': 'application/json',
      'anthropic-ratelimit-requests-remaining': '1000',
      'anthropic-ratelimit-requests-reset': '60',
      'anthropic-ratelimit-tokens-remaining': '100000',
      'anthropic-ratelimit-tokens-reset': '60'
    };
  }

  static createStreamHeader(): Record<string, string> {
    return {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'anthropic-ratelimit-requests-remaining': '1000',
      'anthropic-ratelimit-requests-reset': '60',
      'anthropic-ratelimit-tokens-remaining': '100000',
      'anthropic-ratelimit-tokens-reset': '60'
    };
  }

  static formatStreamChunk(chunk: AnthropicStreamChunk): string {
    return `event: message\ndata: ${JSON.stringify(chunk)}\n\n`;
  }

  static createStreamStart(messageId: string): string {
    const startChunk: AnthropicStreamChunk = {
      type: 'message_start',
      message: {
        id: messageId,
        type: 'message',
        role: 'assistant',
        content: [],
        model: 'claude-3-proxy',
        usage: {
          input_tokens: 0,
          output_tokens: 0
        }
      }
    };
    return this.formatStreamChunk(startChunk);
  }

  static createContentBlockStart(): string {
    const blockStart: AnthropicStreamChunk = {
      type: 'content_block_start',
      index: 0,
      delta: {
        type: 'text'
      }
    };
    return this.formatStreamChunk(blockStart);
  }

  static createStreamStop(): string {
    const stopChunk: AnthropicStreamChunk = {
      type: 'message_stop'
    };
    return this.formatStreamChunk(stopChunk);
  }

  static extractProviderFromModel(model: string, defaultProvider: string): string {
    // Check if model name includes provider prefix (e.g., "ollama/llama2")
    if (model.includes('/')) {
      return model.split('/')[0];
    }

    // Map Claude models to default provider
    if (model.startsWith('claude-')) {
      return defaultProvider;
    }

    // Return default provider for unknown models
    return defaultProvider;
  }

  static extractModelName(model: string, provider: string): string {
    // Remove provider prefix if present
    if (model.includes('/')) {
      const parts = model.split('/');
      return parts.slice(1).join('/');
    }

    return model;
  }
}