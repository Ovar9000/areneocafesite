<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<svelte:head>
	<title>PRIVACY POLICY — LOT 7 CAFE</title>
	<meta name="description" content="Privacy policy for Lot 7 Cafe in Naga City, Camarines Sur. Simple, respectful, and transparent data practices." />
</svelte:head>

<Header />

<main class="legal-page">
	<div class="legal-container container">
		<!-- Breadcrumb / Back Link -->
		<div class="legal-breadcrumb font-mono">
			<a href="/" class="back-home-link">
				<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="15 18 9 12 15 6"></polyline>
				</svg>
				<span>BACK TO LOT 7</span>
			</a>
			<span class="legal-date">EFFECTIVE: 2026</span>
		</div>

		<!-- Title Block -->
		<header class="legal-header">
			<span class="legal-tag font-mono">LEGAL &amp; TRANSPARENCY</span>
			<h1 class="legal-title font-display">PRIVACY POLICY</h1>
			<p class="legal-subtitle font-editorial">
				“A simple, respectful approach to your privacy — in our room and on the web.”
			</p>
		</header>

		<!-- Content Article -->
		<article class="legal-content font-sans">
			<section class="legal-section">
				<h2 class="section-title font-mono">01. OUR CORE PHILOSOPHY</h2>
				<p>
					Lot 7 Cafe (“Lot 7”, “we”, “us”, or “our”) is an independent specialty coffee bar and vinyl listening room based in Naga City, Camarines Sur. We believe your privacy should be handled with the same care and intentionality as our coffee and sound.
				</p>
				<p>
					We do not sell, rent, monetize, or broker personal information. We do not use third-party advertising tracking pixels, cross-site trackers, or invasive data brokers.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">02. INFORMATION WE COLLECT</h2>
				<p>
					We only encounter information that you choose to share with us directly:
				</p>
				<ul>
					<li>
						<strong>Direct Inquiries:</strong> If you contact us via Instagram (<a href="https://instagram.com/lot7.cafe" target="_blank" rel="noopener noreferrer">@lot7.cafe</a>), we use your handle and message solely to answer your questions regarding hours, beans, or listening drops.
					</li>
					<li>
						<strong>In-Store Orders:</strong> In-person transactions at our counter are processed securely through standard point-of-sale terminals. We do not store payment card numbers on our website.
					</li>
				</ul>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">03. COOKIES &amp; WEB ANALYTICS</h2>
				<p>
					Our website is designed to be lightweight, static, and privacy-first. We do not place third-party advertising cookies or trackers on your browser. Any technical storage used is strictly necessary for basic site performance and layout responsiveness.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">04. PHOTOGRAPHY IN OUR CAFE</h2>
				<p>
					Lot 7 is a public community space. From time to time, we capture ambient photographs and short video clips of the room, vinyl turntable sessions, and coffee craftsmanship for our official Instagram stories and archival documentation.
				</p>
				<p>
					We respect our guests’ comfort. If you ever prefer not to be included in ambient room photography or wish for a photo featuring you to be removed from our channels, please speak with our baristas on-site or send a direct message to <a href="https://instagram.com/lot7.cafe" target="_blank" rel="noopener noreferrer">@lot7.cafe</a>.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">05. THIRD-PARTY LINKS</h2>
				<p>
					Our site includes outbound links to external services such as Instagram (<a href="https://instagram.com/lot7.cafe" target="_blank" rel="noopener noreferrer">@lot7.cafe</a>) and map navigation services. These external sites operate under their own independent privacy policies, which we encourage you to review.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">06. CONTACT US</h2>
				<p>
					If you have questions or feedback about our privacy practices, visit us at:
				</p>
				<div class="legal-contact-card font-mono">
					<p class="contact-name">LOT 7 CAFE</p>
					<p class="contact-addr">Naga City, Camarines Sur, Philippines</p>
					<p class="contact-ig">Instagram: <a href="https://instagram.com/lot7.cafe" target="_blank" rel="noopener noreferrer">@lot7.cafe</a></p>
				</div>
			</section>
		</article>
	</div>
</main>

<Footer />

<style>
	.legal-page {
		min-height: calc(100vh - var(--header-height));
		background-color: var(--bg-base);
		padding: 2.5rem 0 5rem;
	}

	.legal-container {
		max-width: 820px;
		margin: 0 auto;
	}

	.legal-breadcrumb {
		display: flex;
		align-items: center;
		justify-content: space-between;
		font-size: 0.72rem;
		letter-spacing: 0.08em;
		margin-bottom: 2rem;
		padding-bottom: 1rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.back-home-link {
		display: inline-flex;
		align-items: center;
		gap: 0.4rem;
		color: var(--text-main);
		text-decoration: none;
		font-weight: 700;
		transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.15s ease;
	}

	.back-home-link:hover {
		color: var(--accent-navy);
		transform: translateX(-3px);
	}

	.legal-date {
		color: var(--text-muted);
	}

	.legal-header {
		margin-bottom: 3rem;
	}

	.legal-tag {
		font-size: 0.72rem;
		font-weight: 700;
		color: var(--accent-navy);
		letter-spacing: 0.12em;
		display: block;
		margin-bottom: 0.5rem;
	}

	.legal-title {
		font-size: clamp(2.5rem, 6vw, 4rem);
		color: var(--text-main);
		line-height: 1;
		margin: 0 0 1rem;
		letter-spacing: -0.02em;
	}

	.legal-subtitle {
		font-size: clamp(1.1rem, 2vw, 1.35rem);
		color: var(--text-secondary);
		line-height: 1.45;
		margin: 0;
	}

	.legal-content {
		display: flex;
		flex-direction: column;
		gap: 2.5rem;
		color: var(--text-secondary);
		font-size: 0.98rem;
		line-height: 1.7;
	}

	.legal-section {
		display: flex;
		flex-direction: column;
		gap: 0.85rem;
		padding-bottom: 2rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.legal-section:last-child {
		border-bottom: none;
		padding-bottom: 0;
	}

	.section-title {
		font-size: 0.85rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		color: var(--text-main);
		margin: 0;
	}

	.legal-section p {
		margin: 0;
	}

	.legal-section ul {
		margin: 0.5rem 0 0.5rem 1.25rem;
		display: flex;
		flex-direction: column;
		gap: 0.65rem;
	}

	.legal-section a {
		color: var(--accent-navy);
		text-decoration: underline;
		text-underline-offset: 3px;
		font-weight: 600;
	}

	.legal-contact-card {
		margin-top: 0.75rem;
		padding: 1.25rem 1.5rem;
		border-radius: var(--radius-card-sm);
		background: var(--bg-surface);
		border: 1px solid var(--border-subtle);
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
		font-size: 0.82rem;
	}

	.contact-name {
		font-weight: 700;
		color: var(--text-main);
	}

	.contact-addr, .contact-ig {
		color: var(--text-secondary);
	}

	@media (max-width: 640px) {
		.legal-page {
			padding: 1.5rem 0 3.5rem;
		}
	}
</style>
