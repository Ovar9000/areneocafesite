import { PAGES, SITE_URL } from '$lib/site';

// Endpoints don't inherit page options from +layout.ts
export const prerender = true;

export function GET() {
	const urls = PAGES.map((path) => `\t<url><loc>${SITE_URL}${path}</loc></url>`).join('\n');

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>
`;

	return new Response(xml, {
		headers: { 'Content-Type': 'application/xml' }
	});
}
