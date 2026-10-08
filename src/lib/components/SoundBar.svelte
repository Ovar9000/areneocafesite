<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';

	const sleeves = [
		{
			title: 'MOVE',
			artist: 'Adam Port, Stryv, Malachiii',
			tag: 'COUNTER ROTATION'
		},
		{
			title: 'SAY WHAT',
			artist: 'feat. Chuala',
			tag: 'COUNTER ROTATION'
		}
	];
</script>

<section class="sound-section" id="sound">
	<div class="sound-inner container">
		<!-- Section Header -->
		<div class="sound-header">
			<div class="section-label">
				<span class="section-label-dot"></span>
				<span>04 / SOUND &amp; VINYL</span>
			</div>
			
			<div class="header-row">
				<h2 class="section-headline">RESIDENT DECK &amp; SLEEVES</h2>
			</div>
		</div>

		<!-- 2-Column Sound Layout -->
		<div class="sound-grid">
			<!-- Column 1: Hardware & Verified Counter Sleeves -->
			<div class="deck-column">
				<div class="turntable-card photo-frame">
					<!-- Portrait source in a landscape frame: keep the selector and the deck in view -->
					<MediaFrame aspect="4 / 3" focus="center 62%" title="The Deck by the Window" detail="Resident night sessions">
						<enhanced:img
							src="$lib/assets/images/dj-night.jpg"
							alt="A DJ playing a set at the Lot 7 deck by the window, with guests looking on"
							sizes="(min-width: 1200px) 580px, (min-width: 900px) 50vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
				</div>

				<!-- Verified Sleeves Photographed On-Site -->
				<div class="sleeves-box photo-frame">
					<div class="sleeves-head font-mono">
						<span>CONFIRMED SLEEVES AT THE BAR</span>
						<span class="status-verified">ON ROTATION</span>
					</div>

					<div class="sleeves-list">
						{#each sleeves as s, i}
							<div class="sleeve-item">
								<span class="sleeve-idx font-mono">0{i + 1}</span>
								<div class="sleeve-info">
									<span class="sleeve-title font-sans">{s.title}</span>
									<span class="sleeve-artist font-sans">{s.artist}</span>
								</div>
								<span class="sleeve-tag font-mono">{s.tag}</span>
							</div>
						{/each}
					</div>
				</div>
			</div>

			<!-- Column 2: Archival Soft-Opening Record (Strictly Dated Past Event) -->
			<div class="archive-column">
				<div class="archive-card photo-frame">
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
						<span class="lineup-label font-mono">SOFT OPENING LINEUP:</span>
						<p class="lineup-names font-display">
							VINZ · PANCAKE · BOS · KIM · SUKI
						</p>

						<div class="archive-subline font-mono">
							<span>POP-UP BY GROOVY</span>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Night Strip: the room once the music is on -->
		<div class="nights-strip">
			<div class="photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 40%" title="In the Mirror" detail="Night sessions">
					<enhanced:img
						src="$lib/assets/images/crowd-mirror.jpg"
						alt="The crowd around the deck, reflected in the room's round convex mirror"
						sizes="(min-width: 1200px) 352px, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>
			<div class="photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 35%" title="Regulars" detail="After hours">
					<enhanced:img
						src="$lib/assets/images/portrait-night.jpg"
						alt="A regular in a plaid shirt caught in warm flash light during a night session"
						sizes="(min-width: 1200px) 352px, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
			</div>
			<div class="photo-frame">
				<MediaFrame aspect="4 / 5" focus="center 45%" title="Hands On" detail="The controller">
					<enhanced:img
						src="$lib/assets/images/dj-controller.jpg"
						alt="Close-up of hands on the DJ controller's jog wheel and pads"
						sizes="(min-width: 1200px) 352px, 31vw"
						loading="lazy"
					/>
				</MediaFrame>
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
		margin-bottom: 3.5rem;
	}

	.header-row {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	@media (min-width: 768px) {
		.header-row {
			flex-direction: row;
			justify-content: space-between;
			align-items: flex-end;
		}
	}

	/* Grid */
	.sound-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2.25rem;
		align-items: flex-start;
	}

	@media (min-width: 900px) {
		.sound-grid {
			grid-template-columns: 1.25fr 1fr;
			gap: 2.75rem;
		}
	}

	.deck-column,
	.archive-column {
		display: flex;
		flex-direction: column;
		gap: 1.75rem;
	}

	/* Night Strip */
	.nights-strip {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 1.5rem;
		margin-top: 2.25rem;
	}

	/* Phones: a tight contact-sheet row instead of three full-height photos */
	@media (max-width: 767px) {
		.nights-strip {
			gap: 0.5rem;
		}

		.nights-strip :global(.media-caption) {
			display: none;
		}

		.nights-strip .photo-frame {
			border-radius: var(--radius-card-sm);
		}
	}

	/* Turntable Card */
	.turntable-card {
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
	}

	/* Sleeves Box */
	.sleeves-box {
		padding: 1.25rem;
		background: var(--bg-surface);
	}

	.sleeves-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
		padding: 0 0.25rem 0.85rem;
	}

	.status-verified {
		color: var(--accent-green);
		font-weight: 700;
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

	.sleeve-tag {
		font-size: 0.7rem;
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

	.archive-subline {
		display: flex;
		flex-direction: column;
		gap: 0.2rem;
		font-size: 0.7rem;
		letter-spacing: 0.08em;
		color: var(--text-muted);
		padding: 0.75rem 1rem;
		border-radius: var(--radius-inner);
		background: var(--bg-subtle);
	}
</style>
