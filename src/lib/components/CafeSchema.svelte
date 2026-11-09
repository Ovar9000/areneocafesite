<script lang="ts">
	import { DAY_NAMES, WEEKLY_HOURS, formatTime24 } from '$lib/hours';
	import { ADD_ONS, MENU, type MenuItem } from '$lib/menu';
	import { ADDRESS, GEO, INSTAGRAM_URL, MAPS_URL, PHONE, SITE_URL } from '$lib/site';

	const menuItem = (item: MenuItem) => ({
		'@type': 'MenuItem',
		name: item.name,
		...(item.notes && { description: item.notes }),
		offers: { '@type': 'Offer', price: item.price, priceCurrency: 'PHP' }
	});

	// schema.org structured data so search engines can show hours, location, menu and links.
	// Hours and menu come from the same tables that drive the page.
	const cafe = {
		'@type': 'CafeOrCoffeeShop',
		'@id': `${SITE_URL}/#cafe`,
		name: 'Lot 7 Cafe',
		alternateName: ['LOT 7 CAFE', 'Lot 7'],
		slogan: 'Your neighborhood, just a little better.',
		description:
			'Espresso, house mixes and cold sodas, with vinyl on the deck, in Naga City, Camarines Sur.',
		url: `${SITE_URL}/`,
		image: `${SITE_URL}/images/og-lot7.jpg`,
		logo: `${SITE_URL}/apple-touch-icon.png`,
		areaServed: { '@type': 'City', name: 'Naga City' },
		currenciesAccepted: 'PHP',
		priceRange: '₱₱',
		servesCuisine: 'Coffee',
		hasMenu: {
			'@type': 'Menu',
			url: `${SITE_URL}/#menu`,
			hasMenuSection: [
				...MENU.map((section) => ({
					'@type': 'MenuSection',
					name: section.title,
					...(section.subtitle && { description: section.subtitle }),
					hasMenuItem: section.items.map(menuItem)
				})),
				{ '@type': 'MenuSection', name: 'Add-ons', hasMenuItem: ADD_ONS.map(menuItem) }
			]
		},
		address: {
			'@type': 'PostalAddress',
			streetAddress: `${ADDRESS.street}, ${ADDRESS.area}`,
			addressLocality: ADDRESS.city,
			postalCode: ADDRESS.postalCode,
			addressRegion: ADDRESS.region,
			addressCountry: 'PH'
		},
		geo: { '@type': 'GeoCoordinates', ...GEO },
		hasMap: MAPS_URL,
		telephone: PHONE.tel,
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

	const website = {
		'@type': 'WebSite',
		'@id': `${SITE_URL}/#website`,
		name: 'Lot 7 Cafe',
		alternateName: ['LOT 7 CAFE', 'lot7.cafe'],
		url: `${SITE_URL}/`,
		inLanguage: 'en-PH',
		publisher: { '@id': `${SITE_URL}/#cafe` }
	};

	const schema = { '@context': 'https://schema.org', '@graph': [website, cafe] };

	// Escape "<" so the JSON can never close the <script> element early
	const json = JSON.stringify(schema).replace(/</g, '\\u003c');
</script>

<svelte:head>
	{@html `<script type="application/ld+json">${json}</script>`}
</svelte:head>
