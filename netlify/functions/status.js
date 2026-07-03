// Weekly capacity counter for Hjemmesidendin
// GET  /.netlify/functions/status            -> { capacity, booked, available }
// POST /.netlify/functions/status?key=ADMIN  -> body { "booked": 2 } sets counter
//      (later: Stripe webhook will increment this automatically)

import { getStore } from "@netlify/blobs";

const CAPACITY = 3;

export default async (req) => {
    const store = getStore("bookings");

    if (req.method === "POST") {
        const url = new URL(req.url);
        const key = url.searchParams.get("key");

        if (!process.env.ADMIN_KEY || key !== process.env.ADMIN_KEY) {
            return new Response(JSON.stringify({ error: "Unauthorized" }), {
                status: 401,
                headers: { "Content-Type": "application/json" }
            });
        }

        const body = await req.json();
        const booked = Math.max(0, Math.min(CAPACITY, parseInt(body.booked, 10) || 0));
        await store.set("booked", String(booked));

        return new Response(JSON.stringify({ ok: true, booked }), {
            headers: { "Content-Type": "application/json" }
        });
    }

    // GET: read current status
    const stored = await store.get("booked");
    const booked = parseInt(stored, 10) || 0;

    return new Response(
        JSON.stringify({
            capacity: CAPACITY,
            booked: booked,
            available: Math.max(0, CAPACITY - booked)
        }),
        { headers: { "Content-Type": "application/json" } }
    );
};