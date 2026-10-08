<script lang="ts">
	import MediaFrame from './MediaFrame.svelte';
	import { ADD_ONS, MENU } from '$lib/menu';

	// Each board section reads like a side of a record
	const SIDES = ['A', 'B', 'C', 'D'];

	// Phones show one side at a time behind A–D tabs instead of four sides stacked. Set only in
	// the browser, so the prerendered page (and anyone without JS) gets the whole board.
	let tabbed = $state(false);
	let active = $state(0);
	const tabs: HTMLButtonElement[] = [];
	let lens = $state<HTMLElement>();

	// The selection is one glass lens that slides between sides. In flight it stretches, turns
	// see-through and catches a highlight, then settles back to solid blue.
	let previous = 0;
	const TINT = '#00388a';
	$effect(() => {
		const to = active;
		if (!lens || to === previous) return;
		previous = to;
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
		// Peak stretch while the lens is moving fastest, then a slow settle back to solid
		// so the see-through moment is long enough to register
		lens.animate(
			[
				{ scale: '1 1', backgroundColor: TINT, easing: 'cubic-bezier(0.3, 0, 0.6, 1)' },
				{ scale: '1.2 0.86', backgroundColor: 'rgba(0, 56, 138, 0.3)', offset: 0.2, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' },
				{ scale: '1 1', backgroundColor: TINT }
			],
			{ duration: 600 }
		);
		lens.animate(
			[
				{ opacity: 0, backgroundPosition: '130% 0' },
				{ opacity: 1, offset: 0.35 },
				{ opacity: 0, backgroundPosition: '-30% 0' }
			],
			{ duration: 650, easing: 'ease-in-out', pseudoElement: '::after' }
		);
	});

	$effect(() => {
		const narrow = window.matchMedia('(max-width: 639px)');
		const sync = () => (tabbed = narrow.matches);
		sync();
		narrow.addEventListener('change', sync);
		return () => narrow.removeEventListener('change', sync);
	});

	// Arrow keys move between tabs (WAI-ARIA tabs pattern)
	function onTabKey(event: KeyboardEvent) {
		const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
		let next: number | undefined;
		if (step) next = (active + step + MENU.length) % MENU.length;
		else if (event.key === 'Home') next = 0;
		else if (event.key === 'End') next = MENU.length - 1;
		if (next === undefined) return;
		event.preventDefault();
		active = next;
		tabs[next].focus();
	}
</script>

<section class="menu-section plates-rest" id="menu">
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
				{#if tabbed}
					<div class="side-tabs" role="tablist" aria-label="Menu sections">
						<span class="side-lens" style:--active={active} bind:this={lens} aria-hidden="true"></span>
						{#each MENU as section, i (section.id)}
							<button
								type="button"
								class="side-tab font-mono"
								role="tab"
								id="menu-tab-{section.id}"
								aria-controls="menu-panel-{section.id}"
								aria-selected={active === i}
								aria-label="Side {SIDES[i]}: {section.title}"
								tabindex={active === i ? 0 : -1}
								onclick={() => (active = i)}
								onkeydown={onTabKey}
								bind:this={tabs[i]}
							>
								SIDE {SIDES[i]}
							</button>
						{/each}
					</div>
				{/if}

				<div class="board-grid">
					{#each MENU as section, i (section.id)}
						<section
							class="board-section"
							id="menu-panel-{section.id}"
							aria-labelledby="menu-{section.id}"
							role={tabbed ? 'tabpanel' : undefined}
							hidden={tabbed && active !== i}
						>
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

	/* The Board: the one hard-edged surface on the page, cut like a plate from the wall:
	   tight corners, a stamped rim and four bolts, against the rounded UI around it */
	.menu-board {
		position: relative;
		background: var(--bg-surface);
		padding: clamp(1.75rem, 4vw, 2.75rem);
		color: var(--brand-blue);
		border-radius: 6px;
	}

	.menu-board::before,
	.menu-board::after {
		content: '';
		position: absolute;
		pointer-events: none;
	}

	/* The stamped rim */
	.menu-board::before {
		inset: 7px;
		border: 1.5px solid rgba(0, 56, 138, 0.16);
		border-radius: 3px;
	}

	/* Bolts, one in each corner */
	.menu-board::after {
		--bolt: radial-gradient(circle, #d9dde5 0 2.5px, #a3abba 3px 3.5px, transparent 4px);
		inset: 12px;
		background:
			var(--bolt) left top / 9px 9px no-repeat,
			var(--bolt) right top / 9px 9px no-repeat,
			var(--bolt) left bottom / 9px 9px no-repeat,
			var(--bolt) right bottom / 9px 9px no-repeat;
	}

	/* Phone-only side switcher: a segmented control above the board */
	.side-tabs {
		--gap: 2px;
		--inset: 3px;
		position: relative;
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: var(--gap);
		margin-bottom: 1.75rem;
		padding: var(--inset);
		border-radius: var(--radius-pill);
		background: var(--fill);
	}

	/* The glass lens under the selected tab: brand blue with a lit top edge and a soft
	   inner shine, so it reads as a pane of tinted glass rather than a flat pill */
	.side-lens {
		position: absolute;
		top: var(--inset);
		bottom: var(--inset);
		left: var(--inset);
		width: calc((100% - 2 * var(--inset) - 3 * var(--gap)) / 4);
		border-radius: var(--radius-pill);
		background-color: var(--tint);
		background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.22), rgba(255, 255, 255, 0) 55%);
		-webkit-backdrop-filter: blur(6px) saturate(180%);
		backdrop-filter: blur(6px) saturate(180%);
		box-shadow:
			inset 0 1px 0 rgba(255, 255, 255, 0.45),
			inset 0 -1px 0 rgba(0, 0, 0, 0.18),
			inset 0 0 0 0.5px rgba(255, 255, 255, 0.25),
			0 4px 12px rgba(0, 56, 138, 0.28);
		translate: calc(var(--active) * (100% + var(--gap))) 0;
		transition: translate 0.52s cubic-bezier(0.32, 0.72, 0, 1);
		overflow: hidden;
		pointer-events: none;
	}

	/* The highlight that crosses the glass while it moves */
	.side-lens::after {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(105deg, transparent 30%, rgba(255, 255, 255, 0.6) 50%, transparent 70%) no-repeat;
		background-size: 250% 100%;
		background-position: 130% 0;
		opacity: 0;
	}

	.side-tab {
		position: relative;
		z-index: 1;
		min-height: 40px;
		border: none;
		border-radius: var(--radius-pill);
		background: transparent;
		color: var(--brand-blue);
		font-size: 0.72rem;
		font-weight: 700;
		letter-spacing: 0.12em;
		cursor: pointer;
		transition: color 0.25s ease;
	}

	/* White once the lens has mostly arrived, so the label never sits white on grey */
	.side-tab[aria-selected='true'] {
		color: #ffffff;
		transition-delay: 0.2s;
	}

	@media (prefers-reduced-motion: reduce) {
		.side-lens {
			transition: none;
		}
	}

	.side-tab:focus-visible {
		outline-offset: 2px;
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
		border-radius: 3px;
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
