import { ProxyError } from '../types';

export class ErrorHandler {
  static handleError(error: any, res: any): void {
    console.error('Proxy error:', error);

    if (error instanceof ProxyError) {
      return res.status(error.statusCode).json({
        error: { type: 'invalid_request_error', message: error.message }
      });
    }

    if (error.code === 'ECONNREFUSED') {
      return res.status(503).json({
        error: { type: 'api_error', message: 'Service unavailable' }
      });
    }

    // Default error
    res.status(500).json({
      error: { type: 'api_error', message: 'Internal server error' }
    });
  }

  static createProxyError(message: string, statusCode: number = 500): ProxyError {
    return new ProxyError(message, statusCode);
  }
}