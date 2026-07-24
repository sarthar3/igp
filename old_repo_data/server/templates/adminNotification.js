/**
 * Admin Notification Email Template
 * Sent to the IGP admin when a new consultation form is submitted.
 */

function adminNotificationTemplate({ name, email, phone, suggestion, submittedAt }) {
  return `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0; padding:0; background-color:#f0f4f8; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f0f4f8; padding:40px 20px;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:16px; overflow:hidden; box-shadow:0 4px 24px rgba(0,0,0,0.08);">
          
          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(135deg, #1e3a5f 0%, #2575c0 50%, #3b82f6 100%); padding:32px 40px; text-align:center;">
              <h1 style="margin:0; color:#ffffff; font-size:24px; font-weight:700; letter-spacing:-0.5px;">
                ⚡ New Consultation Request
              </h1>
              <p style="margin:8px 0 0; color:rgba(255,255,255,0.8); font-size:14px; font-weight:400;">
                Someone wants to connect with IGP
              </p>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:32px 40px;">
              
              <!-- Contact Info Card -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f8fafc; border-radius:12px; border:1px solid #e2e8f0; margin-bottom:24px;">
                <tr>
                  <td style="padding:24px;">
                    <h2 style="margin:0 0 16px; color:#0f172a; font-size:16px; font-weight:600; text-transform:uppercase; letter-spacing:1px;">
                      Contact Details
                    </h2>
                    
                    <!-- Name -->
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:12px;">
                      <tr>
                        <td width="100" style="color:#64748b; font-size:13px; font-weight:600; vertical-align:top; padding:4px 0;">👤 Name</td>
                        <td style="color:#0f172a; font-size:15px; font-weight:500; padding:4px 0;">${escapeHtml(name)}</td>
                      </tr>
                    </table>
                    
                    <!-- Email -->
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:12px;">
                      <tr>
                        <td width="100" style="color:#64748b; font-size:13px; font-weight:600; vertical-align:top; padding:4px 0;">📧 Email</td>
                        <td style="padding:4px 0;">
                          <a href="mailto:${escapeHtml(email)}" style="color:#2575c0; font-size:15px; font-weight:500; text-decoration:none;">${escapeHtml(email)}</a>
                        </td>
                      </tr>
                    </table>
                    
                    <!-- Phone -->
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:0;">
                      <tr>
                        <td width="100" style="color:#64748b; font-size:13px; font-weight:600; vertical-align:top; padding:4px 0;">📱 Phone</td>
                        <td style="padding:4px 0;">
                          <a href="tel:${escapeHtml(phone)}" style="color:#2575c0; font-size:15px; font-weight:500; text-decoration:none;">${escapeHtml(phone)}</a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <!-- Message/Suggestion -->
              ${suggestion ? `
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#fffbeb; border-radius:12px; border:1px solid #fde68a; margin-bottom:24px;">
                <tr>
                  <td style="padding:24px;">
                    <h2 style="margin:0 0 8px; color:#92400e; font-size:13px; font-weight:600; text-transform:uppercase; letter-spacing:1px;">
                      💬 Message / Suggestion
                    </h2>
                    <p style="margin:0; color:#451a03; font-size:14px; line-height:1.6;">
                      ${escapeHtml(suggestion)}
                    </p>
                  </td>
                </tr>
              </table>
              ` : ''}

              <!-- Timestamp -->
              <p style="margin:0; color:#94a3b8; font-size:12px; text-align:center;">
                Submitted on ${submittedAt || new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}
              </p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background:#f8fafc; padding:20px 40px; text-align:center; border-top:1px solid #e2e8f0;">
              <p style="margin:0; color:#94a3b8; font-size:12px;">
                This notification was sent by the IGP Website Contact System
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
  `.trim();
}

/**
 * Simple HTML escaper to prevent XSS in email templates
 */
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

module.exports = { adminNotificationTemplate };
