/**
 * User Confirmation Email Template
 * Auto-reply sent to users after they submit the consultation form.
 */

function userConfirmationTemplate({ name }) {
  const firstName = name ? name.split(' ')[0] : 'there';

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
            <td style="background: linear-gradient(135deg, #1e3a5f 0%, #2575c0 50%, #3b82f6 100%); padding:40px; text-align:center;">
              <h1 style="margin:0; color:#ffffff; font-size:28px; font-weight:700; letter-spacing:-0.5px;">
                IGP by Sparklehood
              </h1>
              <p style="margin:8px 0 0; color:rgba(255,255,255,0.8); font-size:14px;">
                India Growth Partner — Powering EV Infrastructure
              </p>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:40px;">
              <h2 style="margin:0 0 16px; color:#0f172a; font-size:22px; font-weight:600;">
                Hi ${escapeHtml(firstName)}, thanks for reaching out! 👋
              </h2>
              
              <p style="margin:0 0 20px; color:#475569; font-size:15px; line-height:1.7;">
                We've received your consultation request and our team is reviewing it. One of our EV infrastructure experts will get back to you within <strong>24 hours</strong>.
              </p>

              <!-- What's Next Card -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg, #eff6ff, #f0f9ff); border-radius:12px; border:1px solid #bfdbfe; margin-bottom:28px;">
                <tr>
                  <td style="padding:24px;">
                    <h3 style="margin:0 0 12px; color:#1e40af; font-size:14px; font-weight:700; text-transform:uppercase; letter-spacing:1px;">
                      ⚡ What happens next?
                    </h3>
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                      <tr>
                        <td style="padding:6px 0; color:#1e3a8a; font-size:14px; line-height:1.5;">
                          <strong>1.</strong> Our team reviews your requirements
                        </td>
                      </tr>
                      <tr>
                        <td style="padding:6px 0; color:#1e3a8a; font-size:14px; line-height:1.5;">
                          <strong>2.</strong> A dedicated EV specialist is assigned
                        </td>
                      </tr>
                      <tr>
                        <td style="padding:6px 0; color:#1e3a8a; font-size:14px; line-height:1.5;">
                          <strong>3.</strong> We schedule a free consultation call
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <p style="margin:0 0 28px; color:#475569; font-size:14px; line-height:1.7;">
                In the meantime, feel free to explore our services or reach us directly at
                <a href="mailto:team@sparklehood.com" style="color:#2575c0; text-decoration:none; font-weight:600;">team@sparklehood.com</a>
              </p>

              <!-- CTA Button -->
              <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;">
                <tr>
                  <td style="background:linear-gradient(135deg, #2575c0, #3b82f6); border-radius:50px; text-align:center;">
                    <a href="https://igpsparklehood.com" style="display:inline-block; padding:14px 36px; color:#ffffff; font-size:14px; font-weight:600; text-decoration:none; letter-spacing:0.5px;">
                      Explore Our Services →
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Social -->
          <tr>
            <td style="padding:0 40px 20px; text-align:center;">
              <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;">
                <tr>
                  <td style="padding:0 8px;">
                    <a href="https://www.instagram.com/igp.sparklehood/" style="color:#64748b; text-decoration:none; font-size:13px;">Instagram</a>
                  </td>
                  <td style="color:#cbd5e1;">•</td>
                  <td style="padding:0 8px;">
                    <a href="https://www.linkedin.com/company/igp-by-sparklehood/" style="color:#64748b; text-decoration:none; font-size:13px;">LinkedIn</a>
                  </td>
                  <td style="color:#cbd5e1;">•</td>
                  <td style="padding:0 8px;">
                    <a href="https://www.facebook.com/sparklehoodteam/" style="color:#64748b; text-decoration:none; font-size:13px;">Facebook</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background:#f8fafc; padding:20px 40px; text-align:center; border-top:1px solid #e2e8f0;">
              <p style="margin:0; color:#94a3b8; font-size:12px;">
                © ${new Date().getFullYear()} India Growth Partner by Sparklehood. All rights reserved.
              </p>
              <p style="margin:6px 0 0; color:#94a3b8; font-size:11px;">
                This is an automated response. Please do not reply to this email.
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

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

module.exports = { userConfirmationTemplate };
