<script lang="ts">
	import Seo from '$lib/components/Seo.svelte';
	import CafeSchema from '$lib/components/CafeSchema.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import TheStory from '$lib/components/TheStory.svelte';
	import TheRoom from '$lib/components/TheRoom.svelte';
	import Menu from '$lib/components/Menu.svelte';
	import SoundBar from '$lib/components/SoundBar.svelte';
	import Gallery from '$lib/components/Gallery.svelte';
	import VisitUs from '$lib/components/VisitUs.svelte';
</script>

<Seo
	title="LOT 7 CAFE — Your neighborhood, just a little better."
	description="Lot 7 Cafe in Naga City, Camarines Sur: your neighborhood, just a little better. Espresso classics, house mixes and sodas from ₱99, with a resident deck. Open Monday to Saturday, 10 AM to 10 PM."
/>
<CafeSchema />

<Hero />
<TheStory />
<TheRoom />
<Menu />
<SoundBar />
<Gallery />
<VisitUs />
