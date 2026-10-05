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

<section class="sound-section paper-texture" id="sound">
	<div class="sound-inner container">
		<!-- Section Header -->
		<div class="sound-header">
			<div class="section-label">
				<span class="section-label-dot"></span>
				<span>03 / SOUND &amp; VINYL</span>
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
					<MediaFrame aspect="4 / 3" tags={['RESIDENT DECK', 'STUDIO MONITORS']}>
						<enhanced:img
							src="$lib/assets/images/turntable-setup.jpg"
							alt="Resident Turntable Deck &amp; Studio Monitors at Lot 7"
							sizes="(min-width: 1200px) 580px, (min-width: 900px) 50vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>

					<div class="turntable-details">
						<h3 class="card-heading font-sans">DIRECT-DRIVE ANALOG DECK</h3>
					</div>
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
							<span>“YOUR NEIGHBORHOOD, JUST A LITTLE BETTER.”</span>
						</div>
					</div>
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
		background-color: var(--bg-surface);
		border-top: 1px solid var(--border-subtle);
		border-bottom: 1px solid var(--border-subtle);
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

	/* Turntable Card */
	.turntable-card {
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.turntable-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

	.turntable-details {
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.card-heading {
		font-size: 1.2rem;
		font-weight: 700;
		color: var(--text-main);
	}

	/* Sleeves Box */
	.sleeves-box {
		padding: 1.5rem;
		background: var(--bg-surface);
	}

	.sleeves-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
		padding-bottom: 0.75rem;
		border-bottom: 1px solid var(--border-subtle);
		margin-bottom: 1rem;
	}

	.status-verified {
		color: var(--accent-green);
		font-weight: 700;
	}

	.sleeves-list {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.sleeve-item {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.75rem 1rem;
		background: var(--bg-subtle);
		border-radius: var(--radius-card-sm);
		border: 1px solid var(--border-subtle);
	}

	.sleeve-idx {
		font-size: 0.75rem;
		font-weight: 700;
		color: var(--accent-navy);
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
		padding: 1.75rem;
		background: var(--bg-surface);
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
	}

	.archive-card:hover {
		box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
		border-color: var(--border-mid);
	}

	.archive-top {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 0.7rem;
		letter-spacing: 0.1em;
		padding-bottom: 0.5rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	.archive-pill {
		color: var(--accent-navy);
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
		background: #14213d;
		padding: 1rem;
		display: flex;
		justify-content: center;
		position: relative;
	}

	/* Frosted glass light sweep across the poster tile */
	.archive-poster-wrap::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(
			115deg,
			transparent 35%,
			rgba(255, 255, 255, 0.28) 50%,
			transparent 65%
		);
		transform: translateX(-100%);
		transition: transform 0.75s var(--ease-out);
		pointer-events: none;
		z-index: 3;
	}

	.archive-poster {
		max-height: 290px;
		width: auto;
		object-fit: contain;
		display: block;
		border-radius: 4px;
		transition: transform 0.65s var(--ease-out);
	}

	.archive-card:hover .archive-poster {
		transform: scale(1.04);
	}

	.archive-card:hover .archive-poster-wrap::before {
		transform: translateX(100%);
	}

	.archive-caption {
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
		padding: 0.5rem 0;
		border-top: 1px dashed var(--border-subtle);
		border-bottom: 1px dashed var(--border-subtle);
	}
</style>
