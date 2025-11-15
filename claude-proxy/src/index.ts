import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import routes from './routes';
import { config } from './config';
import { ErrorHandler } from './utils/errors';
import { performanceMonitor, performanceConfig, checkSystemHealth } from './utils/performance';

// Load environment variables
dotenv.config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Performance monitoring middleware
app.use(performanceMonitor);

// Routes
app.use('/', routes);

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    error: {
      type: 'not_found_error',
      message: 'The requested resource was not found'
    }
  });
});

// Global error handler
app.use((error: any, req: express.Request, res: express.Response, next: express.NextFunction) => {
  ErrorHandler.handleError(error, res);
});

// Start server
const port = config.port;

const server = app.listen(port, () => {
  console.log(`Claude Proxy Server running on port ${port}`);
  console.log(`Health check: http://localhost:${port}/health`);
  console.log(`Providers: http://localhost:${port}/providers`);
  console.log(`Default provider: ${config.defaultProvider}`);
});

// Configure server for performance
server.keepAliveTimeout = performanceConfig.keepAliveTimeout;
server.headersTimeout = performanceConfig.headersTimeout;

export default app;