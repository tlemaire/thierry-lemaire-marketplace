// Anthropic API Types
export interface AnthropicMessage {
  role: 'user' | 'assistant';
  content: Array<{
    type: 'text' | 'image';
    text?: string;
    source?: {
      type: 'base64';
      media_type: string;
      data: string;
    };
  }>;
}

export interface AnthropicRequest {
  model: string;
  max_tokens: number;
  messages: AnthropicMessage[];
  system?: string;
  temperature?: number;
  top_p?: number;
  top_k?: number;
  stop_sequences?: string[];
  stream?: boolean;
}

export interface AnthropicResponse {
  id: string;
  type: 'message';
  role: 'assistant';
  content: Array<{
    type: 'text';
    text: string;
  }>;
  model: string;
  stop_reason: 'end_turn' | 'max_tokens' | 'stop_sequence';
  stop_sequence?: string;
  usage: {
    input_tokens: number;
    output_tokens: number;
  };
}

export interface AnthropicStreamChunk {
  type: 'message_start' | 'content_block_start' | 'content_block_delta' | 'content_block_stop' | 'message_delta' | 'message_stop';
  index?: number;
  delta?: {
    type?: string;
    text?: string;
    stop_reason?: string;
    stop_sequence?: string;
  };
  usage?: {
    input_tokens?: number;
    output_tokens?: number;
  };
  message?: {
    id: string;
    type: string;
    role: string;
    content: Array<any>;
    model: string;
    stop_reason?: string;
    stop_sequence?: string;
    usage?: {
      input_tokens: number;
      output_tokens: number;
    };
  };
}

// Provider Types
export interface ProviderRequest {
  model: string;
  messages: Array<{
    role: string;
    content: string;
  }>;
  temperature?: number;
  max_tokens?: number;
  stream?: boolean;
  system?: string;
}

export interface ProviderResponse {
  choices: Array<{
    message: {
      role: string;
      content: string;
    };
    finish_reason: string;
  }>;
  usage: {
    prompt_tokens: number;
    completion_tokens: number;
    total_tokens: number;
  };
  model: string;
}

export interface ProviderStreamChunk {
  choices: Array<{
    delta: {
      content?: string;
      role?: string;
    };
    finish_reason?: string;
  }>;
  usage?: {
    prompt_tokens?: number;
    completion_tokens?: number;
    total_tokens?: number;
  };
}

// Configuration Types
export interface ProviderConfig {
  name: string;
  baseUrl: string;
  apiKey?: string;
  model: string;
  headers?: Record<string, string>;
}

export interface ProxyConfig {
  port: number;
  defaultProvider: string;
  providers: Record<string, ProviderConfig>;
  modelMapping: Record<string, Record<string, string>>;
}

// Error Types
export class ProxyError extends Error {
  constructor(
    message: string,
    public statusCode: number = 500
  ) {
    super(message);
    this.name = 'ProxyError';
  }
}