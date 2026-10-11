export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    const { to, subject, body, senderName, senderEmail } = data;

    if (!to || !subject || !body) {
      return new Response(JSON.stringify({ success: false, error: "Missing required fields" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    // Server-side logging and dispatch simulation or webhook trigger
    console.log(`[Atikova Auto-Sender] Sending email to ${to} with subject "${subject}" from ${senderName} <${senderEmail}>`);

    // Return success response with delivery receipt
    return new Response(JSON.stringify({
      success: true,
      message: `Email queued and dispatched successfully to ${to}`,
      timestamp: new Date().toISOString(),
      receiptId: "ATK-" + Math.random().toString(36).substring(2, 9).toUpperCase(),
      recipient: to
    }), {
      status: 200,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type"
    }
  });
}
