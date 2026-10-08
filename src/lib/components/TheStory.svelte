<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
</script>

<section class="story-section" id="story">
	<div class="story-inner container">
		<!-- Section Header -->
		<div class="section-label">
			<span class="section-label-dot"></span>
			<span>01 / THE MANIFESTO</span>
		</div>

		<!-- Editorial Spread -->
		<div class="story-layout">
			<!-- Left: The Verbatim Manifesto Copy -->
			<div class="story-copy">
				<blockquote class="manifesto-quote">
					<p class="quote-lead font-sans">
						Every space starts with a feeling.
					</p>

					<p class="quote-body font-sans">
						From the cafes we admired to the experiences that stayed with us, Lot 7 grew from a collection of ideas, music, and feelings.
					</p>

					<p class="quote-closing font-editorial">
						“But what inspires us is only where the story begins.”
					</p>
				</blockquote>
			</div>

			<!-- Right: The room under the tagline ceiling, in true portrait ratio -->
			<div class="story-media photo-frame">
				<MediaFrame aspect="3 / 4" maxHeight="560px" title="The Room" detail="Under the tagline">
					<enhanced:img
						src="$lib/assets/images/room-fisheye.jpg"
						alt="Wide view of the Lot 7 room: guests at the tables beneath the ceiling lettering 'your neighborhood, just a little better.'"
						sizes="(min-width: 1200px) 452px, (min-width: 850px) 38vw, 92vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>
		</div>
	</div>
</section>

<style>
	.story-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		position: relative;
		box-sizing: border-box;
	}

	.story-layout {
		display: grid;
		grid-template-columns: 1fr;
		gap: 3.5rem;
		align-items: center;
		margin-top: 1.5rem;
	}

	@media (min-width: 850px) {
		.story-layout {
			grid-template-columns: 1.25fr 1fr;
			gap: 4.5rem;
		}
	}

	/* Copy Column */
	.story-copy {
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.manifesto-quote {
		display: flex;
		flex-direction: column;
		gap: 1.85rem;
	}

	.quote-lead {
		font-size: clamp(2.2rem, 4vw, 3.4rem);
		font-weight: 700;
		letter-spacing: -0.03em;
		line-height: 1.05;
		color: var(--text-main);
	}

	.quote-body {
		font-size: clamp(1.05rem, 1.8vw, 1.25rem);
		line-height: 1.65;
		color: var(--text-secondary);
		max-width: 520px;
	}

	.quote-closing {
		font-size: clamp(1.2rem, 2.2vw, 1.45rem);
		color: var(--tint);
		line-height: 1.45;
		border-left: 2px solid var(--tint);
		padding-left: 1.25rem;
	}
</style>
