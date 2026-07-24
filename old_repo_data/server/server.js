/**
 * IGP Backend Server
 * Express.js server with Resend email integration.
 * 
 * Run: npm run dev (development) or npm start (production)
 */

require('dotenv').config();

const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');

const emailRoutes = require('./routes/email');

// --- App Setup ---
const app = express();
const PORT = process.env.PORT || 3001;

// --- Middleware ---

// CORS — allow requests from the frontend
const allowedOrigins = [
  'http://127.0.0.1:5500',
  'http://localhost:5500',
  'http://127.0.0.1:5501',
  'http://localhost:5501',
  'http://localhost:3000',
  'https://igp-flax.vercel.app',
  // Strip trailing slash from FRONTEND_URL (browsers send origin without it)
  process.env.FRONTEND_URL ? process.env.FRONTEND_URL.replace(/\/+$/, '') : null
].filter(Boolean);

app.use(cors({
  origin: function (origin, callback) {
    // Allow requests with no origin (mobile apps, curl, etc.)
    if (!origin) return callback(null, true);
    if (allowedOrigins.includes(origin)) {
      return callback(null, true);
    }
    return callback(new Error('Not allowed by CORS'), false);
  },
  methods: ['GET', 'POST'],
  credentials: true
}));

// Parse JSON bodies
app.use(express.json({ limit: '1mb' }));

// Parse URL-encoded bodies
app.use(express.urlencoded({ extended: true }));

// --- Rate Limiting ---
const emailLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 5,                     // max 5 submissions per window per IP
  message: {
    success: false,
    error: 'Too many submissions. Please wait 15 minutes before trying again.'
  },
  standardHeaders: true,
  legacyHeaders: false,
});

// --- Routes ---

// Health check
app.get('/api/health', (req, res) => {
  res.status(200).json({
    status: 'ok',
    service: 'IGP Email Backend',
    timestamp: new Date().toISOString(),
    uptime: `${Math.floor(process.uptime())}s`
  });
});

// Email routes (rate limited)
app.use('/api', emailLimiter, emailRoutes);

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: `Route ${req.method} ${req.originalUrl} not found.`
  });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error('💥 Unhandled error:', err.message);
  res.status(500).json({
    success: false,
    error: 'Internal server error.'
  });
});

// --- Start Server ---
app.listen(PORT, () => {
  console.log('');
  console.log('  ⚡ IGP Backend Server');
  console.log('  ────────────────────────────');
  console.log(`  🌐 Server:   http://localhost:${PORT}`);
  console.log(`  💚 Health:   http://localhost:${PORT}/api/health`);
  console.log(`  📧 Contact:  POST http://localhost:${PORT}/api/contact`);
  console.log(`  📋 Career:   POST http://localhost:${PORT}/api/career`);
  console.log('  ────────────────────────────');
  console.log(`  🔑 Resend:   ${process.env.RESEND_API_KEY ? 'Configured ✓' : 'Missing ✗'}`);
  console.log(`  📬 Admin:    ${process.env.ADMIN_EMAIL || 'Not set'}`);
  console.log('');
});

module.exports = app;
