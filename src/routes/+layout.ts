import { dev } from '$app/environment';
import { injectAnalytics } from '@vercel/analytics/sveltekit';
import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';

export const prerender = true;
export const ssr = true;

// Vercel Web Analytics and Speed Insights. Both load their scripts from this site's own
// /_vercel/* paths, so the CSP needs no new sources. They only report once the matching
// feature is switched on for the project in the Vercel dashboard.
injectAnalytics({ mode: dev ? 'development' : 'production' });
injectSpeedInsights();
