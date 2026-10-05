<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
</script>

<section class="story-section paper-texture" id="story">
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

			<!-- Right: Storefront Glass Photograph in True Portrait Ratio -->
			<div class="story-media photo-frame">
				<MediaFrame aspect="3 / 4" maxHeight="560px" tags={['STOREFRONT GLASS', 'ENTRANCE']}>
					<enhanced:img
						src="$lib/assets/images/storefront-window.jpg"
						alt="Lot 7 Cafe Storefront Window Glass Decal"
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
		background-color: var(--bg-surface);
		border-top: 1px solid var(--border-subtle);
		border-bottom: 1px solid var(--border-subtle);
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
		color: var(--accent-navy);
		line-height: 1.45;
		border-left: 2px solid var(--accent-navy);
		padding-left: 1.25rem;
	}

	/* Media Column */
	.story-media {
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.story-media:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

</style>
