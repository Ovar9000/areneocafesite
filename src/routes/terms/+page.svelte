<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<svelte:head>
	<title>TERMS OF SERVICE — LOT 7 CAFE</title>
	<meta name="description" content="Terms of service and room guidelines for Lot 7 Cafe in Naga City, Camarines Sur. Specialty coffee, listening room etiquette, and house principles." />
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
			<span class="legal-tag font-mono">HOUSE GUIDELINES &amp; POLICIES</span>
			<h1 class="legal-title font-display">TERMS OF SERVICE</h1>
			<p class="legal-subtitle font-editorial">
				“Mutual respect, intentional listening, and a neighborhood space for everyone.”
			</p>
		</header>

		<!-- Content Article -->
		<article class="legal-content font-sans">
			<section class="legal-section">
				<h2 class="section-title font-mono">01. WELCOME TO LOT 7</h2>
				<p>
					These Terms of Service govern your access to and use of Lot 7 Cafe’s website and physical premises in Naga City, Camarines Sur. By stepping into our cafe or viewing our digital showcase, you agree to these principles designed to protect our community atmosphere.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">02. HOUSE ETIQUETTE &amp; SOUND CULTURE</h2>
				<p>
					Lot 7 is centered around music, vinyl listening, and coffee craft. To ensure a welcoming experience for all guests:
				</p>
				<ul>
					<li>
						<strong>Audio Equipment &amp; Turntables:</strong> Our vinyl collection, turntables, and sound gear are operated exclusively by Lot 7 staff and authorized guest selectors. Please refrain from handling records or audio equipment unless invited.
					</li>
					<li>
						<strong>Shared Atmosphere:</strong> We encourage meaningful conversation, reading, and listening. We ask guests to keep personal phone calls, laptop speaker playback, and volume considerate of neighboring tables.
					</li>
					<li>
						<strong>Seating &amp; Tables:</strong> Seating is available on a first-come, first-served basis. During high-traffic hours, we appreciate cooperation in sharing larger tables when appropriate.
					</li>
				</ul>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">03. MENU OFFERINGS &amp; EVENTS</h2>
				<p>
					All coffee beverages, beans, seasonal drinks, and pastry offerings are subject to availability.
				</p>
				<p>
					Listening sessions, guest selector appearances, and opening hours may adjust based on private events or holiday schedules. Real-time updates and unannounced drops are communicated through our Instagram stories (<a href="https://instagram.com/lot7.cafe" target="_blank" rel="noopener noreferrer">@lot7.cafe</a>).
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">04. INTELLECTUAL PROPERTY &amp; BRANDING</h2>
				<p>
					The Lot 7 name, crest, badge logos, storefront window typography, original graphic designs, and digital media are the exclusive property of Lot 7 Cafe. Unauthorized commercial use, reproduction, or modification without prior written consent is prohibited.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">05. GUEST CONDUCT &amp; RIGHT OF ADMISSION</h2>
				<p>
					We take pride in fostering an inclusive, respectful neighborhood gathering place. We reserve the right to refuse service or ask individuals to leave if their behavior is disruptive, abusive, or harmful to fellow guests or staff.
				</p>
			</section>

			<section class="legal-section">
				<h2 class="section-title font-mono">06. GOVERNING LAW</h2>
				<p>
					These terms are governed by and construed in accordance with the laws of the Republic of the Philippines.
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
