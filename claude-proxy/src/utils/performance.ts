import { Request, Response, NextFunction } from 'express';

// Performance monitoring middleware
export function performanceMonitor(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - startTime;
    console.log(`${req.method} ${req.path} - ${duration}ms - ${res.statusCode}`);
  });

  next();
}

// Performance configuration
export const performanceConfig = {
  requestTimeout: 300000,
  maxConcurrentRequests: 100,
  keepAliveTimeout: 65000,
  headersTimeout: 66000,
};

export function checkSystemHealth() {
  const memUsage = process.memoryUsage();

  return {
    status: 'healthy',
    memory: {
      rss: `${Math.round(memUsage.rss / 1024 / 1024)}MB`,
      heapUsed: `${Math.round(memUsage.heapUsed / 1024 / 1024)}MB`,
    }
  };
}