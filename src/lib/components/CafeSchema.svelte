<script lang="ts">
	import { DAY_NAMES, WEEKLY_HOURS, formatTime24 } from '$lib/hours';
	import { INSTAGRAM_URL, MAPS_URL, SITE_URL } from '$lib/site';

	// schema.org structured data so search engines can show hours, location and links.
	// Hours come from the same table that drives the live open/closed status.
	const schema = {
		'@context': 'https://schema.org',
		'@type': 'CafeOrCoffeeShop',
		name: 'Lot 7 Cafe',
		description:
			'Specialty coffee, resident vinyl listening, and natural light in Naga City, Camarines Sur.',
		url: `${SITE_URL}/`,
		image: `${SITE_URL}/images/brand-cafe-lounge.jpg`,
		address: {
			'@type': 'PostalAddress',
			addressLocality: 'Naga City',
			addressRegion: 'Camarines Sur',
			addressCountry: 'PH'
		},
		hasMap: MAPS_URL,
		sameAs: [INSTAGRAM_URL],
		acceptsReservations: false,
		openingHoursSpecification: WEEKLY_HOURS.flatMap((hours, day) =>
			hours
				? [
						{
							'@type': 'OpeningHoursSpecification',
							dayOfWeek: DAY_NAMES[day],
							opens: formatTime24(hours.open),
							closes: formatTime24(hours.close)
						}
					]
				: []
		)
	};

	// Escape "<" so the JSON can never close the <script> element early
	const json = JSON.stringify(schema).replace(/</g, '\\u003c');
</script>

<svelte:head>
	{@html `<script type="application/ld+json">${json}</script>`}
</svelte:head>
