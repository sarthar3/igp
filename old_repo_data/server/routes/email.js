/**
 * Email Routes — /api/contact and /api/career
 * Handles form submissions and sends emails via Resend.
 */

const express = require('express');
const { Resend } = require('resend');
const { adminNotificationTemplate } = require('../templates/adminNotification');
const { userConfirmationTemplate } = require('../templates/userConfirmation');

const router = express.Router();

// Initialize Resend client
const resend = new Resend(process.env.RESEND_API_KEY);

// Config
const ADMIN_EMAIL = process.env.ADMIN_EMAIL || 'sarveshtharun3388@gmail.com';
const SENDER_EMAIL = process.env.SENDER_EMAIL || 'onboarding@resend.dev';
const SENDER_NAME = process.env.SENDER_NAME || 'IGP by Sparklehood';

/**
 * POST /api/contact
 * Handles consultation form submissions from the main website.
 */
router.post('/contact', async (req, res) => {
  try {
    const { name, email, phone, suggestion } = req.body;

    // --- Validation ---
    if (!name || !email || !phone) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields: name, email, and phone are required.'
      });
    }

    // Basic email format validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format.'
      });
    }

    // Basic phone validation (at least 10 digits)
    const phoneDigits = phone.replace(/\D/g, '');
    if (phoneDigits.length < 10) {
      return res.status(400).json({
        success: false,
        error: 'Phone number must have at least 10 digits.'
      });
    }

    const submittedAt = new Date().toLocaleString('en-IN', {
      timeZone: 'Asia/Kolkata',
      dateStyle: 'full',
      timeStyle: 'short'
    });

    // --- Send Admin Notification Email ---
    const adminEmailResult = await resend.emails.send({
      from: `${SENDER_NAME} <${SENDER_EMAIL}>`,
      to: [ADMIN_EMAIL],
      subject: `🔔 New Consultation Request from ${name}`,
      html: adminNotificationTemplate({ name, email, phone, suggestion, submittedAt })
    });

    console.log('✅ Admin notification sent:', adminEmailResult);

    // --- Send User Confirmation Email ---
    let userEmailResult = null;
    try {
      userEmailResult = await resend.emails.send({
        from: `${SENDER_NAME} <${SENDER_EMAIL}>`,
        to: [email],
        subject: `Thanks for reaching out to IGP by Sparklehood! ⚡`,
        html: userConfirmationTemplate({ name })
      });
      console.log('✅ User confirmation sent:', userEmailResult);
    } catch (userEmailError) {
      // Don't fail the whole request if user confirmation fails
      console.warn('⚠️ User confirmation email failed (non-critical):', userEmailError.message);
    }

    // --- Success Response ---
    return res.status(200).json({
      success: true,
      message: 'Your consultation request has been received! Check your email for confirmation.',
      data: {
        adminEmail: adminEmailResult?.data?.id || null,
        userEmail: userEmailResult?.data?.id || null
      }
    });

  } catch (error) {
    console.error('❌ Contact form error:', error);
    return res.status(500).json({
      success: false,
      error: 'Failed to process your request. Please try again later.'
    });
  }
});

/**
 * POST /api/career
 * Handles career page job application submissions.
 */
router.post('/career', async (req, res) => {
  try {
    const { name, email, phone, position, message } = req.body;

    // --- Validation ---
    if (!name || !email || !phone) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields: name, email, and phone are required.'
      });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format.'
      });
    }

    const submittedAt = new Date().toLocaleString('en-IN', {
      timeZone: 'Asia/Kolkata',
      dateStyle: 'full',
      timeStyle: 'short'
    });

    // --- Send Career Application Notification to Admin ---
    const careerEmailHtml = `
      <div style="font-family:sans-serif; max-width:600px; margin:0 auto; padding:20px;">
        <div style="background:linear-gradient(135deg,#1e3a5f,#2575c0); padding:24px 32px; border-radius:12px 12px 0 0;">
          <h1 style="color:#fff; margin:0; font-size:20px;">📋 New Career Application</h1>
        </div>
        <div style="background:#fff; padding:24px 32px; border:1px solid #e2e8f0; border-top:none; border-radius:0 0 12px 12px;">
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> <a href="mailto:${email}">${email}</a></p>
          <p><strong>Phone:</strong> <a href="tel:${phone}">${phone}</a></p>
          ${position ? `<p><strong>Position:</strong> ${position}</p>` : ''}
          ${message ? `<p><strong>Message:</strong><br>${message}</p>` : ''}
          <hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">
          <p style="color:#94a3b8; font-size:12px;">Submitted on ${submittedAt}</p>
        </div>
      </div>
    `;

    const result = await resend.emails.send({
      from: `${SENDER_NAME} <${SENDER_EMAIL}>`,
      to: [ADMIN_EMAIL],
      subject: `📋 Career Application: ${name}${position ? ` — ${position}` : ''}`,
      html: careerEmailHtml
    });

    console.log('✅ Career application notification sent:', result);

    return res.status(200).json({
      success: true,
      message: 'Your application has been received! We\'ll review it and get back to you.',
      data: { emailId: result?.data?.id || null }
    });

  } catch (error) {
    console.error('❌ Career form error:', error);
    return res.status(500).json({
      success: false,
      error: 'Failed to submit your application. Please try again later.'
    });
  }
});

module.exports = router;
