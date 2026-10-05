<script lang="ts">
	import { page } from '$app/state';
	import { SITE_NAME, SITE_URL } from '$lib/site';

	interface Props {
		title: string;
		description: string;
		/** Site-relative image path for link previews */
		image?: string;
		imageAlt?: string;
	}

	let {
		title,
		description,
		image = '/images/brand-cafe-lounge.jpg',
		imageAlt = 'Interior seating and lounge at Lot 7 Cafe'
	}: Props = $props();

	// Built from the fixed production origin so prerendered HTML and preview deploys
	// always point crawlers at https://lot7.cafe
	let canonical = $derived(new URL(page.url.pathname, SITE_URL).href);
	let imageUrl = $derived(new URL(image, SITE_URL).href);
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="description" content={description} />
	<link rel="canonical" href={canonical} />

	<meta property="og:site_name" content={SITE_NAME} />
	<meta property="og:type" content="website" />
	<meta property="og:locale" content="en_PH" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:url" content={canonical} />
	<meta property="og:image" content={imageUrl} />
	<meta property="og:image:alt" content={imageAlt} />
	<meta name="twitter:card" content="summary_large_image" />
</svelte:head>
