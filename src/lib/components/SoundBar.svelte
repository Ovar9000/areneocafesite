<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';

	const sleeves = [
		{ title: 'MOVE', artist: 'Adam Port, Stryv, Malachiii' },
		{ title: 'SAY WHAT', artist: 'feat. Chuala' }
	];
</script>

<section class="sound-section" id="sound">
	<div class="sound-inner container">
		<!-- Section Header -->
		<div class="sound-header">
			<h2 class="section-headline">RESIDENT DECK &amp; SLEEVES</h2>
		</div>

		<!-- Ordered grid. Desktop: the deck and the poster share row one at the same height;
		     row two is four equal tiles (three night photos and the records on rotation).
		     Phones: deck, poster, the photos as one row, then the records. -->
		<div class="sound-bento">
			<div class="tile tile-deck photo-frame">
				<!-- Portrait source in a landscape frame: keep the selector and the deck in view -->
				<MediaFrame aspect="4 / 3" focus="center 62%" title="The Deck by the Window" detail="Resident night sessions">
					<enhanced:img
						src="$lib/assets/images/dj-night.jpg"
						alt="A DJ playing a set at the Lot 7 deck by the window, with guests looking on"
						sizes="(min-width: 1200px) 640px, (min-width: 900px) 55vw, 92vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>

			<div class="tile tile-poster archive-card photo-frame">
				<div class="archive-top font-mono">
					<span class="archive-pill">PAST EVENTS</span>
					<span class="archive-date font-mono">09.08.26 · 5:00 PM</span>
				</div>

				<div class="archive-poster-wrap">
					<enhanced:img
						src="$lib/assets/images/soft-opening-poster.jpg"
						alt="Lot 7 Soft Opening Poster: 09.08.26 featuring Vinz, Pancake, Bos, Kim, Suki"
						class="archive-poster"
						width="434"
						loading="lazy"
					/>
				</div>

				<div class="archive-caption">
					<span class="lineup-label font-mono">SOFT OPENING LINEUP · POP-UP BY GROOVY</span>
					<p class="lineup-names font-display">VINZ · PANCAKE · BOS · KIM · SUKI</p>
				</div>
			</div>

			<div class="tile tile-night photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 40%" title="In the Mirror" detail="Night sessions">
					<enhanced:img
						src="$lib/assets/images/crowd-mirror.jpg"
						alt="The crowd around the deck, reflected in the room's round convex mirror"
						sizes="(min-width: 1200px) 270px, (min-width: 900px) 23vw, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>
			<div class="tile tile-night photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 35%" title="Regulars" detail="After hours">
					<enhanced:img
						src="$lib/assets/images/portrait-night.jpg"
						alt="A regular in a plaid shirt caught in warm flash light during a night session"
						sizes="(min-width: 1200px) 270px, (min-width: 900px) 23vw, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>
			<div class="tile tile-night photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 45%" title="Hands On" detail="The controller">
					<enhanced:img
						src="$lib/assets/images/dj-controller.jpg"
						alt="Close-up of hands on the DJ controller's jog wheel and pads"
						sizes="(min-width: 1200px) 270px, (min-width: 900px) 23vw, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>

			<!-- Records photographed at the bar -->
			<div class="tile tile-sleeves sleeves-box photo-frame">
				<div class="sleeves-head">
					<span class="status-verified font-mono"><span class="status-dot"></span>ON ROTATION</span>
					<span class="sleeves-title font-sans">Sleeves at the bar</span>
				</div>

				<div class="sleeves-list">
					{#each sleeves as s, i}
						<div class="sleeve-item">
							<span class="sleeve-idx font-mono">0{i + 1}</span>
							<div class="sleeve-info">
								<span class="sleeve-title font-sans">{s.title}</span>
								<span class="sleeve-artist font-sans">{s.artist}</span>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.sound-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		position: relative;
		box-sizing: border-box;
	}

	.sound-header {
		margin-bottom: 2.5rem;
	}

	/* The ordered grid: 12 columns on desktop, 6 below */
	.sound-bento {
		display: grid;
		grid-template-columns: repeat(6, 1fr);
		gap: 1rem;
	}

	.tile-deck,
	.tile-poster,
	.tile-sleeves {
		grid-column: span 6;
	}

	.tile-night {
		grid-column: span 2;
	}

	/* Phones: the three photos read as one contact-sheet row */
	@media (max-width: 899px) {
		.tile-night {
			border-radius: var(--radius-card-sm);
		}

		.tile-night :global(.media-caption) {
			display: none;
		}
	}

	@media (min-width: 900px) {
		.sound-bento {
			grid-template-columns: repeat(12, 1fr);
			gap: 1.5rem;
		}

		.tile-deck {
			grid-column: span 7;
		}

		.tile-poster {
			grid-column: span 5;
		}

		.tile-night,
		.tile-sleeves {
			grid-column: span 3;
		}

		/* Row one: the poster card sets the height and the deck photo fills it. The photo is
		   taken out of flow so its own proportions can't stretch the row. */
		.tile-deck {
			position: relative;
			min-height: 360px;
		}

		.tile-deck :global(.media-frame) {
			position: absolute;
			inset: 0;
			aspect-ratio: auto !important;
			height: 100%;
		}
	}

	/* Sleeves Box */
	.sleeves-box {
		padding: 1.25rem;
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.sleeves-head {
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
		padding: 0.35rem 0.25rem 0;
	}

	.status-verified {
		display: inline-flex;
		align-items: center;
		gap: 0.45rem;
		font-size: 0.68rem;
		letter-spacing: 0.14em;
		color: var(--accent-green);
		font-weight: 700;
	}

	.status-dot {
		width: 7px;
		height: 7px;
		border-radius: 50%;
		background: #34c759;
		box-shadow: 0 0 0 3px rgba(52, 199, 89, 0.18);
	}

	.sleeves-title {
		font-size: 1.15rem;
		font-weight: 700;
		color: var(--text-main);
	}

	/* iOS inset grouped list: one rounded group, rows split by inset hairlines */
	.sleeves-list {
		display: flex;
		flex-direction: column;
		background: var(--bg-subtle);
		border-radius: var(--radius-card-sm);
		overflow: hidden;
	}

	.sleeve-item {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.8rem 1rem;
		position: relative;
	}

	.sleeve-item + .sleeve-item::before {
		content: '';
		position: absolute;
		top: 0;
		left: 2.9rem;
		right: 0;
		border-top: 1px solid var(--border-subtle);
	}

	.sleeve-idx {
		font-size: 0.75rem;
		font-weight: 700;
		color: var(--tint);
	}

	.sleeve-info {
		flex: 1;
		display: flex;
		flex-direction: column;
	}

	.sleeve-title {
		font-size: 0.95rem;
		font-weight: 700;
		color: var(--text-main);
	}

	.sleeve-artist {
		font-size: 0.78rem;
		color: var(--text-muted);
	}
	/* Archival Card */
	.archive-card {
		padding: 1.25rem;
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
	}

	.archive-top {
		padding: 0.35rem 0.5rem 0;
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.7rem;
		letter-spacing: 0.1em;
	}

	.archive-pill {
		color: var(--tint);
		font-weight: 700;
	}

	.archive-date {
		color: var(--accent-amber-text);
		font-weight: 700;
	}

	.archive-poster-wrap {
		width: 100%;
		border-radius: var(--radius-card-sm);
		overflow: hidden;
		background: var(--tint);
		padding: 1rem;
		display: flex;
		justify-content: center;
		position: relative;
	}

	.archive-poster {
		max-height: 290px;
		width: auto;
		object-fit: contain;
		display: block;
		border-radius: 6px;
	}

	.archive-caption {
		padding: 0 0.5rem 0.35rem;
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.lineup-label {
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
	}

	.lineup-names {
		font-size: clamp(1.4rem, 2.5vw, 1.85rem);
		letter-spacing: 0.04em;
		color: var(--text-main);
		line-height: 1.05;
	}
</style>
