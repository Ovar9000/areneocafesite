<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
	import { ADD_ONS, MENU } from '$lib/menu';

	// Each board section reads like a side of a record
	const SIDES = ['A', 'B', 'C', 'D'];
</script>

<section class="menu-section" id="menu">
	<div class="menu-inner container">
		<!-- Section Header -->
		<div class="menu-header">

			<div class="header-row">
				<h2 class="section-headline">ON THE BOARD</h2>
				<p class="header-note font-mono">PRICES IN PHILIPPINE PESOS · ₱</p>
			</div>
		</div>

		<div class="menu-layout">
			<!-- Photo Column: what actually comes across the bar -->
			<div class="menu-photos">
				<div class="photo-frame menu-photo-main">
					<MediaFrame aspect="4 / 5" focus="center 62%" title="House Cup" detail="Iced">
						<enhanced:img
							src="$lib/assets/images/drink-cup.jpg"
							alt="An iced coffee in a Lot 7 cup, set down on the bar"
							sizes="(min-width: 1200px) 400px, (min-width: 980px) 34vw, 92vw"
							loading="lazy"
						/>
					</MediaFrame>
				</div>

				<div class="menu-photo-pair">
					<div class="photo-frame">
						<MediaFrame aspect="1 / 1" focus="center 45%">
							<enhanced:img
								src="$lib/assets/images/drink-pour.jpg"
								alt="Milk being poured over espresso and ice"
								sizes="(min-width: 1200px) 192px, (min-width: 980px) 16vw, 45vw"
								loading="lazy"
							/>
						</MediaFrame>
					</div>
					<div class="photo-frame">
						<MediaFrame aspect="1 / 1" focus="center 58%">
							<enhanced:img
								src="$lib/assets/images/drink-soda.jpg"
								alt="A green soda in a Lot 7 cup on the counter"
								sizes="(min-width: 1200px) 192px, (min-width: 980px) 16vw, 45vw"
								loading="lazy"
							/>
						</MediaFrame>
					</div>
				</div>
			</div>

			<!-- The Board -->
			<div class="menu-board photo-frame">
				<div class="board-grid">
					{#each MENU as section, i (section.id)}
						<section class="board-section" aria-labelledby="menu-{section.id}">
							<header class="board-section-head">
								<span class="side-tag font-mono" aria-hidden="true">SIDE {SIDES[i]}</span>
								<h3 id="menu-{section.id}" class="board-title font-sans">{section.title}</h3>
								{#if section.subtitle}
									<p class="board-subtitle font-mono">{section.subtitle}</p>
								{/if}
							</header>

							<ul class="board-items">
								{#each section.items as item (item.name)}
									<li class="board-item">
										<div class="item-line">
											<span class="item-name font-sans">{item.name}</span>
											<span class="item-leader" aria-hidden="true"></span>
											<span class="item-price font-mono"><span class="peso">₱</span>{item.price}</span>
										</div>
										{#if item.notes}
											<span class="item-notes font-editorial">{item.notes}</span>
										{/if}
									</li>
								{/each}
							</ul>
						</section>
					{/each}
				</div>

				<!-- Add-ons run along the bottom of the board -->
				<div class="board-addons">
					<h3 class="addons-title font-mono">ADD-ONS</h3>
					<ul class="addons-list">
						{#each ADD_ONS as addon (addon.name)}
							<li class="addon font-sans">
								<span>{addon.name}</span>
								<span class="item-price font-mono"><span class="peso">+₱</span>{addon.price}</span>
							</li>
						{/each}
					</ul>
				</div>

				<p class="board-foot font-mono">MENU MAY CHANGE · ASK AT THE BAR FOR TODAY'S POUR</p>
			</div>
		</div>
	</div>
</section>

<style>
	.menu-section {
		min-height: 100dvh;
		display: flex;
		align-items: center;
		padding: 5.5rem 0;
		position: relative;
		box-sizing: border-box;
	}

	.menu-header {
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

	.header-note {
		font-size: 0.7rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
	}

	/* Layout: photos beside the board on desktop, a strip above it on phones */
	.menu-layout {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2rem;
		align-items: start;
	}

	@media (min-width: 980px) {
		.menu-layout {
			grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.45fr);
			gap: 2.5rem;
		}

		.menu-photos {
			position: sticky;
			top: calc(var(--header-height) + 1.5rem);
		}
	}

	.menu-photos {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.menu-photo-pair {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1rem;
	}

	/* Phones: one row of three square-ish crops keeps the board close to the top */
	@media (max-width: 979px) {
		.menu-photos {
			display: grid;
			grid-template-columns: 1.3fr 1fr;
			gap: 0.75rem;
		}

		.menu-photos .photo-frame {
			border-radius: var(--radius-card-sm);
		}

		.menu-photo-main :global(.media-frame) {
			aspect-ratio: auto !important;
			height: 100%;
		}

		.menu-photo-pair {
			grid-template-columns: 1fr;
			gap: 0.75rem;
		}

		.menu-photo-main :global(.media-caption) {
			display: none;
		}
	}

	/* The Board */
	.menu-board {
		background: var(--bg-surface);
		padding: clamp(1.5rem, 4vw, 2.75rem);
		color: var(--brand-blue);
	}

	.board-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 2.5rem;
	}

	@media (min-width: 640px) {
		.board-grid {
			grid-template-columns: 1fr 1fr;
			column-gap: clamp(2rem, 4vw, 3.5rem);
			row-gap: 2.75rem;
		}
	}

	.board-section-head {
		display: flex;
		flex-direction: column;
		gap: 0.3rem;
		padding-bottom: 0.9rem;
		margin-bottom: 1.1rem;
		border-bottom: 1px dotted currentColor;
	}

	.side-tag {
		font-size: 0.66rem;
		font-weight: 700;
		letter-spacing: 0.2em;
		color: var(--accent-amber-text);
	}

	.board-title {
		font-size: clamp(1.3rem, 2.2vw, 1.6rem);
		font-weight: 700;
		letter-spacing: -0.02em;
		line-height: 1.1;
		text-transform: uppercase;
		color: var(--brand-blue);
	}

	.board-subtitle {
		font-size: 0.68rem;
		letter-spacing: 0.14em;
		text-transform: uppercase;
		color: var(--text-muted);
	}

	.board-items {
		list-style: none;
		display: flex;
		flex-direction: column;
		gap: 0.85rem;
	}

	.board-item {
		display: flex;
		flex-direction: column;
		gap: 0.1rem;
	}

	.item-line {
		display: flex;
		align-items: baseline;
		gap: 0.6rem;
	}

	.item-name {
		font-size: 1rem;
		font-weight: 600;
		letter-spacing: 0.01em;
		text-transform: uppercase;
		color: var(--brand-blue);
	}

	/* Dotted leader between the drink and its price */
	.item-leader {
		flex: 1;
		min-width: 1.5rem;
		border-bottom: 1.5px dotted rgba(0, 56, 138, 0.35);
		transform: translateY(-0.28em);
	}

	.item-price {
		font-size: 0.95rem;
		font-weight: 700;
		font-variant-numeric: tabular-nums;
		color: var(--brand-blue);
		white-space: nowrap;
	}

	.peso {
		font-weight: 500;
		font-size: 0.8em;
		margin-right: 0.1em;
		opacity: 0.7;
	}

	.item-notes {
		font-size: 0.95rem;
		color: var(--text-secondary);
		line-height: 1.3;
	}

	/* Add-ons strip */
	.board-addons {
		display: flex;
		flex-direction: column;
		gap: 0.85rem;
		margin-top: 2.75rem;
		padding: 1.1rem 1.25rem;
		border-radius: var(--radius-card-sm);
		background: var(--tint-soft);
	}

	@media (min-width: 640px) {
		.board-addons {
			flex-direction: row;
			align-items: center;
			gap: 1.75rem;
		}
	}

	.addons-title {
		font-size: 0.7rem;
		font-weight: 700;
		letter-spacing: 0.18em;
		color: var(--brand-blue);
		flex-shrink: 0;
	}

	.addons-list {
		list-style: none;
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem 1.75rem;
	}

	.addon {
		display: inline-flex;
		align-items: baseline;
		gap: 0.5rem;
		font-size: 0.92rem;
		font-weight: 600;
		text-transform: uppercase;
		color: var(--brand-blue);
	}

	.addon .item-price {
		font-size: 0.85rem;
	}

	.board-foot {
		margin-top: 1.5rem;
		font-size: 0.66rem;
		letter-spacing: 0.12em;
		color: var(--text-muted);
	}
</style>
