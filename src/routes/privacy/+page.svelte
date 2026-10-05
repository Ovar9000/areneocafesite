<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import LegalPage from '$lib/components/LegalPage.svelte';
	import { INSTAGRAM_URL } from '$lib/site';
</script>

<Seo
	title="PRIVACY POLICY — LOT 7 CAFE"
	description="Privacy policy for Lot 7 Cafe in Naga City, Camarines Sur. Simple, respectful, and transparent data practices."
/>

<LegalPage
	tag="LEGAL & TRANSPARENCY"
	title="PRIVACY POLICY"
	subtitle="A simple, respectful approach to your privacy — in our room and on the web."
	effective="2026"
>
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
				<strong>Direct Inquiries:</strong> If you contact us via Instagram (<a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a>), we use your handle and message solely to answer your questions regarding hours, beans, or listening drops.
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
			We respect our guests’ comfort. If you ever prefer not to be included in ambient room photography or wish for a photo featuring you to be removed from our channels, please speak with our baristas on-site or send a direct message to <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a>.
		</p>
	</section>

	<section class="legal-section">
		<h2 class="section-title font-mono">05. THIRD-PARTY LINKS</h2>
		<p>
			Our site includes outbound links to external services such as Instagram (<a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a>) and map navigation services. These external sites operate under their own independent privacy policies, which we encourage you to review.
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
			<p class="contact-ig">Instagram: <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer">@lot7.cafe</a></p>
		</div>
	</section>
</LegalPage>
