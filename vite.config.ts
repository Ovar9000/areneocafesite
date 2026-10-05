import adapter from '@sveltejs/adapter-static';
import { enhancedImages } from '@sveltejs/enhanced-img';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	build: {
		// Never inline fonts as data: URIs; the CSP allows fonts from 'self' only,
		// and separate files cache better than base64 inside the CSS
		assetsInlineLimit: (filePath) => (/\.(woff2?|ttf|otf)$/.test(filePath) ? false : undefined)
	},
	plugins: [
		// Build-time AVIF/WebP/JPEG + srcset for <enhanced:img> (must run before sveltekit)
		enhancedImages(),
		sveltekit({
			compilerOptions: {
				// Force runes mode for the project, except for libraries.
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules') ? undefined : true
			},
			adapter: adapter({
				// Served by Vercel for unknown URLs; renders the +error page client-side
				fallback: '404.html'
			}),
			// Prerendered pages receive this as a <meta http-equiv> tag, with a sha256 hash
			// for SvelteKit's inline bootstrap script, so script-src needs no 'unsafe-inline'.
			// Header-only protections (frame-ancestors, X-Frame-Options, etc.) live in vercel.json.
			csp: {
				mode: 'hash',
				directives: {
					'default-src': ['self'],
					'script-src': ['self'],
					// Svelte writes inline style attributes
					'style-src': ['self', 'unsafe-inline'],
					'font-src': ['self'],
					'img-src': ['self', 'data:'],
					'media-src': ['self'],
					'connect-src': ['self'],
					'object-src': ['none'],
					'base-uri': ['self'],
					'form-action': ['self'],
					'upgrade-insecure-requests': true
				}
			}
		})
	]
});
