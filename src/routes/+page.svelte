<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import CafeSchema from '$lib/components/CafeSchema.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import TheStory from '$lib/components/TheStory.svelte';
	import Menu from '$lib/components/Menu.svelte';
	import SoundBar from '$lib/components/SoundBar.svelte';
	import Gallery from '$lib/components/Gallery.svelte';
	import VisitUs from '$lib/components/VisitUs.svelte';
</script>

<Seo
	title="Lot 7 Cafe, Naga City | your neighborhood, just a little better."
	description="Lot 7 Cafe in Naga City. Espresso, house mixes and cold sodas from ₱99, and vinyl on the deck. Open Mon–Fri 10 AM–10 PM, Sat 2 PM–10 PM."
/>
<CafeSchema />

<Hero />
<TheStory />
<Gallery />
<Menu />
<SoundBar />
<VisitUs />
