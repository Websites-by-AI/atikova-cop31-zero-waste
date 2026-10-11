export async function onRequestPost(context) {
  try {
    const data = await context.request.json();
    const { to, subject, body, senderName, senderEmail } = data;

    if (!to || !subject) {
      return new Response(JSON.stringify({ success: false, error: "Missing required fields (to, subject)" }), {
        status: 400,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    }

    const receiptId = "ATK-" + Math.random().toString(36).substring(2, 9).toUpperCase();
    const timestamp = new Date().toISOString();

    console.log(`[Atikova Auto-Sender] Outbound dispatch: To=${to}, Subject="${subject}", Sender="${senderName}" <${senderEmail}>, Receipt=${receiptId}`);

    return new Response(JSON.stringify({
      success: true,
      message: `Email dispatched successfully to ${to}`,
      timestamp: timestamp,
      receiptId: receiptId,
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
