<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import TheStory from '$lib/components/TheStory.svelte';
	import TheRoom from '$lib/components/TheRoom.svelte';
	import SoundBar from '$lib/components/SoundBar.svelte';
	import VisitUs from '$lib/components/VisitUs.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<svelte:head>
	<title>LOT 7 CAFE — Every space starts with a feeling.</title>
	<meta name="description" content="Lot 7 Cafe in Naga City, Camarines Sur. Every space starts with a feeling. Specialty coffee, resident vinyl listening, and natural light." />
	<meta property="og:type" content="website" />
	<meta property="og:title" content="LOT 7 CAFE" />
	<meta property="og:description" content="Every space starts with a feeling. Specialty coffee, resident vinyl listening, and natural light in Naga City." />
	<meta property="og:image" content="/images/interior-lounge-wide.png" />
	<meta name="twitter:card" content="summary_large_image" />
</svelte:head>

<Header />

<main id="main-content">
	<Hero />
	<TheStory />
	<TheRoom />
	<SoundBar />
	<VisitUs />
</main>

<Footer />
