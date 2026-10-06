<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import LegalPage from '$lib/components/LegalPage.svelte';
	import { INSTAGRAM_URL } from '$lib/site';
</script>

<Seo
	title="TERMS OF SERVICE — LOT 7 CAFE"
	description="Terms of service and room guidelines for Lot 7 Cafe in Naga City, Camarines Sur. Specialty coffee, listening room etiquette, and house principles."
/>

<LegalPage
	tag="HOUSE GUIDELINES & POLICIES"
	title="TERMS OF SERVICE"
	subtitle="Mutual respect, intentional listening, and a neighborhood space for everyone."
	effective="2026"
>
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
			Listening sessions, guest selector appearances, and opening hours may adjust based on private events or holiday schedules. Real-time announcements and updates are communicated through our Instagram stories (<a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a>).
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
			<p class="contact-ig">Instagram: <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a></p>
		</div>
	</section>
</LegalPage>
