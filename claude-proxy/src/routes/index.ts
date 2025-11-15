import express from 'express';
import messagesRouter from './messages';

const router = express.Router();

// Health check endpoint
router.get('/health', (req, res) => {
  const { checkSystemHealth } = require('../utils/performance');
  const systemHealth = checkSystemHealth();

  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: '1.0.0',
    system: systemHealth,
    provider: require('../config').config.defaultProvider
  });
});

// Provider info endpoint
router.get('/providers', (req, res) => {
  const { ProviderFactory } = require('../providers');
  res.json({
    supported_providers: ProviderFactory.getSupportedProviders(),
    default_provider: require('../config').config.defaultProvider
  });
});

// Mount messages router
router.use('/v1', messagesRouter);

export default router;