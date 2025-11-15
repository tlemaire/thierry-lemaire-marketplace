#!/usr/bin/env node

// Simple benchmark for Claude Proxy with vLLM
const http = require('http');
const { performance } = require('perf_hooks');

const config = {
  concurrentRequests: 10,
  totalRequests: 100,
  testMessage: {
    model: 'vllm/Qwen/Qwen3-Next',
    messages: [
      { role: 'user', content: 'Write a Python function for binary search.' }
    ],
    max_tokens: 200,
    temperature: 0.7
  }
};

async function makeRequest(requestData) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify(requestData);

    const options = {
      hostname: 'localhost',
      port: 3000,
      path: '/v1/messages',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const startTime = performance.now();
    const req = http.request(options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        const endTime = performance.now();
        resolve({
          statusCode: res.statusCode,
          duration: endTime - startTime
        });
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function runBenchmark() {
  console.log(`Benchmark: ${config.totalRequests} requests, ${config.concurrentRequests} concurrent`);

  const results = [];
  const startTime = performance.now();

  for (let i = 0; i < config.totalRequests; i += config.concurrentRequests) {
    const batch = Math.min(config.concurrentRequests, config.totalRequests - i);
    const promises = [];

    for (let j = 0; j < batch; j++) {
      promises.push(makeRequest(config.testMessage));
    }

    try {
      const batchResults = await Promise.all(promises);
      results.push(...batchResults);
      console.log(`Batch ${Math.floor(i / config.concurrentRequests) + 1} completed`);
    } catch (error) {
      console.error(`Batch failed:`, error.message);
    }
  }

  const totalTime = performance.now() - startTime;
  const durations = results.map(r => r.duration);
  const avgDuration = durations.reduce((a, b) => a + b, 0) / durations.length;
  const successRate = (results.filter(r => r.statusCode === 200).length / results.length) * 100;
  const throughput = (results.length / totalTime) * 1000;

  console.log('\nResults:');
  console.log(`Success rate: ${successRate.toFixed(2)}%`);
  console.log(`Average duration: ${avgDuration.toFixed(2)}ms`);
  console.log(`Throughput: ${throughput.toFixed(2)} req/s`);
}

async function checkServer() {
  try {
    await makeRequest({ ...config.testMessage, max_tokens: 10 });
    console.log('Server running, starting benchmark...');
    await runBenchmark();
  } catch (error) {
    console.error('Server not available. Start with: npm run dev');
    process.exit(1);
  }
}

checkServer();