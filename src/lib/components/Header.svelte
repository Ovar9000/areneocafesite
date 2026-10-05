<script lang="ts">
	import Lot7Logo from './Lot7Logo.svelte';
	import { clickSpring } from '$lib/attachments/click-spring';
	import { INSTAGRAM_URL } from '$lib/site';

	let scrolled = $state(false);
	let mobileOpen = $state(false);
	let drawer: HTMLDialogElement;

	$effect(() => {
		const handleScroll = () => {
			scrolled = window.scrollY > 20;
		};

		// The drawer only exists in the mobile layout; close it if the viewport grows past it
		const desktopQuery = window.matchMedia('(min-width: 900px)');
		const handleBreakpoint = (e: MediaQueryListEvent) => {
			if (e.matches) closeMobile();
		};

		// Enable touch active states on mobile WebKit
		const noop = () => {};

		document.body.addEventListener('touchstart', noop, { passive: true });
		window.addEventListener('scroll', handleScroll, { passive: true });
		desktopQuery.addEventListener('change', handleBreakpoint);
		handleScroll();

		return () => {
			document.body.removeEventListener('touchstart', noop);
			window.removeEventListener('scroll', handleScroll);
			desktopQuery.removeEventListener('change', handleBreakpoint);
		};
	});

	// showModal() gives focus trapping, Escape-to-close, an inert background
	// and focus return to the toggle button for free.
	function openMobile() {
		drawer.showModal();
		mobileOpen = true;
	}

	function closeMobile() {
		drawer.close();
	}

	// Fires for every close path: close button, links, backdrop click and Escape
	function handleDrawerClose() {
		mobileOpen = false;
	}

	function handleBackdropClick(e: MouseEvent) {
		// The dialog's own children cover its whole box, so a click whose
		// target is the dialog itself landed on the ::backdrop
		if (e.target === drawer) closeMobile();
	}
</script>

<header class="site-header" class:scrolled>
	<div class="header-inner container">
		<!-- Left: Hamburger on Mobile / Brand Logo on Desktop -->
		<div class="header-left">
			<button 
				type="button" 
				class="mobile-toggle"
				onclick={openMobile}
				aria-label="Open navigation menu"
				aria-haspopup="dialog"
				aria-controls="site-drawer"
				aria-expanded={mobileOpen}
			>
				<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
					<line x1="3" y1="6" x2="21" y2="6"></line>
					<line x1="3" y1="12" x2="21" y2="12"></line>
					<line x1="3" y1="18" x2="21" y2="18"></line>
				</svg>
			</button>

			<a href="/" class="brand-link desktop-only-brand" aria-label="Lot 7 Cafe home">
				<Lot7Logo height="36px" />
			</a>
		</div>

		<!-- Mobile Centered Brand Logo (Matches Fat Seed Mascot style) -->
		<a href="/" class="brand-link mobile-center-brand" class:drawer-open={mobileOpen} aria-label="Lot 7 Cafe home">
			<Lot7Logo height="32px" />
		</a>

		<!-- Center: Desktop In-Page Jumps -->
		<nav class="desktop-nav font-sans" aria-label="Page Sections">
			<a href="/#story" class="nav-item">THE STORY</a>
			<a href="/#room" class="nav-item">THE ROOM</a>
			<a href="/#sound" class="nav-item">SOUND</a>
			<a href="/#visit" class="nav-item">VISIT</a>
		</nav>

		<!-- Right: Primary Instagram Door Only -->
		<div class="header-actions">
			<a 
				href={INSTAGRAM_URL} 
				target="_blank" 
				rel="noopener noreferrer" 
				class="ig-link font-mono"
				class:drawer-open={mobileOpen}
				{@attach clickSpring}
				aria-label="Follow Lot 7 on Instagram @lot7.cafe"
			>
				<svg class="ig-svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
					<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
					<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
				</svg>
				<span class="ig-handle">@lot7.cafe</span>
			</a>
		</div>
	</div>
</header>

<!-- Sideswipe Navigation Drawer: a native modal dialog that slides in from the left.
     Escape closes it natively, so the backdrop click handler needs no key equivalent. -->
<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
	bind:this={drawer}
	id="site-drawer"
	class="sideswipe-drawer"
	aria-label="Site navigation"
	onclose={handleDrawerClose}
	onclick={handleBackdropClick}
>
	<!-- Drawer Header with Logo & Circular Close Button -->
	<div class="drawer-header">
		<a href="/" onclick={closeMobile} class="drawer-logo" aria-label="Lot 7 Cafe home">
			<Lot7Logo height="34px" />
		</a>

		<!-- svelte-ignore a11y_autofocus -->
		<button
			type="button"
			class="drawer-close-btn"
			onclick={closeMobile}
			aria-label="Close navigation menu"
			autofocus
		>
			<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
				<line x1="18" y1="6" x2="6" y2="18"></line>
				<line x1="6" y1="6" x2="18" y2="18"></line>
			</svg>
		</button>
	</div>

	<!-- Drawer Navigation Links -->
	<div class="drawer-body">
		<nav class="drawer-nav font-sans" aria-label="Page sections">
			<a href="/#story" onclick={closeMobile} class="drawer-nav-item">
				<span class="nav-idx font-mono">01</span>
				<span class="nav-text">THE STORY</span>
				<svg class="nav-arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="9 18 15 12 9 6"></polyline>
				</svg>
			</a>
			<a href="/#room" onclick={closeMobile} class="drawer-nav-item">
				<span class="nav-idx font-mono">02</span>
				<span class="nav-text">THE ROOM</span>
				<svg class="nav-arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="9 18 15 12 9 6"></polyline>
				</svg>
			</a>
			<a href="/#sound" onclick={closeMobile} class="drawer-nav-item">
				<span class="nav-idx font-mono">03</span>
				<span class="nav-text">SOUND &amp; VINYL</span>
				<svg class="nav-arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="9 18 15 12 9 6"></polyline>
				</svg>
			</a>
			<a href="/#visit" onclick={closeMobile} class="drawer-nav-item">
				<span class="nav-idx font-mono">04</span>
				<span class="nav-text">VISIT US &amp; HOURS</span>
				<svg class="nav-arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<polyline points="9 18 15 12 9 6"></polyline>
				</svg>
			</a>
		</nav>

		<!-- Drawer Footer & Instagram -->
		<div class="drawer-footer">
			<a 
				href={INSTAGRAM_URL} 
				target="_blank" 
				rel="noopener noreferrer" 
				class="drawer-ig-cta font-mono"
				{@attach clickSpring}
			>
				<svg class="ig-svg-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
					<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
					<line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
				</svg>
				<span>FOLLOW @LOT7.CAFE</span>
			</a>

			<div class="drawer-location font-mono">
				<span>NAGA CITY · CAMARINES SUR</span>
			</div>
		</div>
	</div>
</dialog>

<style>
	.site-header {
		position: sticky;
		top: 0;
		left: 0;
		right: 0;
		z-index: 1000;
		background: rgba(250, 250, 247, 0.94);
		backdrop-filter: blur(14px);
		-webkit-backdrop-filter: blur(14px);
		border-bottom: 1px solid var(--border-subtle);
		transition: background-color 0.25s ease, box-shadow 0.25s ease;
	}

	.site-header.scrolled {
		background: rgba(255, 255, 255, 0.98);
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
	}

	.header-inner {
		display: flex;
		align-items: center;
		justify-content: space-between;
		height: var(--header-height);
		gap: 1rem;
		position: relative;
	}

	.header-left {
		display: flex;
		align-items: center;
	}

	/* Brand Badge Desktop */
	.brand-link {
		display: flex;
		align-items: center;
		text-decoration: none;
		user-select: none;
		cursor: pointer;
		transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
		will-change: transform;
	}

	.brand-link:hover {
		transform: translateY(-2px) scale(1.04);
	}

	.brand-link:active {
		transform: translateY(1.5px) scale(0.92);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	.desktop-only-brand {
		display: none;
	}

	/* Mobile Center Logo */
	.mobile-center-brand {
		display: flex;
		position: absolute;
		left: 50%;
		transform: translateX(-50%) translateY(0) scale(1);
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.25s ease;
		will-change: transform, opacity;
	}

	.mobile-center-brand:hover {
		transform: translateX(-50%) translateY(-2px) scale(1.04);
	}

	.mobile-center-brand:active {
		transform: translateX(-50%) translateY(1.5px) scale(0.92);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	.mobile-center-brand.drawer-open {
		transform: translateX(-50%) scale(0.85);
		opacity: 0;
		pointer-events: none;
	}

	@media (min-width: 900px) {
		.desktop-only-brand {
			display: flex;
		}

		.mobile-center-brand {
			display: none;
		}
	}

	/* Desktop Nav */
	.desktop-nav {
		display: none;
		align-items: center;
		gap: 2.25rem;
	}

	@media (min-width: 900px) {
		.desktop-nav {
			display: flex;
		}
	}

	.nav-item {
		font-size: 0.82rem;
		font-weight: 600;
		letter-spacing: 0.05em;
		color: var(--text-secondary);
		text-decoration: none;
		padding: 0.35rem 0.25rem;
		user-select: none;
		transition: color 0.15s ease, transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
		will-change: transform;
	}

	.nav-item:hover {
		color: var(--text-main);
		transform: translateY(-1.5px);
		text-decoration: underline;
		text-underline-offset: 4px;
	}

	.nav-item:active {
		transform: translateY(1px) scale(0.95);
		transition-duration: 0.06s;
	}

	/* Header Actions & Instagram Button */
	.header-actions {
		display: flex;
		align-items: center;
		gap: 0.85rem;
	}

	.ig-link {
		display: inline-flex;
		align-items: center;
		gap: 0.48rem;
		padding: 0.45rem 0.95rem;
		border-radius: var(--radius-pill);
		border: 1px solid var(--border-subtle);
		background: var(--bg-surface);
		color: var(--text-main);
		font-size: 0.75rem;
		font-weight: 600;
		text-decoration: none;
		user-select: none;
		box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), 
		            opacity 0.25s ease,
		            box-shadow 0.25s ease, 
		            background-color 0.2s ease, 
		            color 0.2s ease, 
		            border-color 0.2s ease;
		will-change: transform, opacity;
	}

	.ig-link.drawer-open {
		transform: scale(0.85);
		opacity: 0;
		pointer-events: none;
	}

	.ig-link :global(.ig-svg-icon) {
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
		flex-shrink: 0;
	}

	.ig-link:hover {
		border-color: var(--accent-navy);
		background: var(--accent-navy);
		color: #ffffff;
		transform: translateY(-2.5px) scale(1.04);
		box-shadow: 0 8px 22px rgba(20, 33, 61, 0.22);
	}

	.ig-link:hover :global(.ig-svg-icon) {
		transform: rotate(-12deg) scale(1.2);
	}

	.ig-link:active {
		transform: translateY(2px) scale(0.91);
		box-shadow: 0 2px 4px rgba(20, 33, 61, 0.12);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.08s ease;
	}

	.ig-link:active :global(.ig-svg-icon) {
		transform: rotate(0deg) scale(0.92);
		transition: transform 0.08s ease;
	}

	@media (max-width: 640px) {
		.ig-handle {
			display: none;
		}
		.ig-link {
			padding: 0.45rem;
			border-radius: 50%;
			width: 38px;
			height: 38px;
			justify-content: center;
		}
	}

	/* Mobile Toggle Button */
	.mobile-toggle {
		display: flex;
		align-items: center;
		justify-content: center;
		background: transparent;
		border: 1px solid var(--border-subtle);
		color: var(--text-main);
		width: 40px;
		height: 40px;
		border-radius: 50%;
		cursor: pointer;
		user-select: none;
		transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), 
		            background-color 0.2s ease, 
		            border-color 0.2s ease, 
		            color 0.2s ease;
		will-change: transform;
	}

	.mobile-toggle:hover {
		background: var(--bg-surface);
		border-color: var(--text-main);
		transform: scale(1.06);
	}

	.mobile-toggle:active {
		transform: scale(0.88);
		background: var(--bg-subtle);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	@media (min-width: 900px) {
		.mobile-toggle {
			display: none;
		}
	}

	/* =========================================
	   SIDESWIPE NAVIGATION DRAWER ANIMATION
	   ========================================= */

	/* Lock page scroll behind the open drawer */
	:global(body:has(dialog.sideswipe-drawer[open])) {
		overflow: hidden;
	}

	/* Sideswipe Drawer: a modal <dialog> that slides in from the left.
	   `display` and `overlay` transition discretely so the exit animation
	   plays before the dialog leaves the top layer. */
	.sideswipe-drawer {
		position: fixed;
		inset: 0 auto 0 0;
		width: min(85vw, 360px);
		max-width: none;
		height: 100dvh;
		max-height: none;
		margin: 0;
		padding: 0;
		border: none;
		border-right: 1px solid var(--border-subtle);
		background: #ffffff;
		color: var(--text-main);
		flex-direction: column;
		transform: translateX(-100%);
		box-shadow: none;
		transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
		            box-shadow 0.4s ease,
		            overlay 0.4s allow-discrete,
		            display 0.4s allow-discrete;
	}

	/* display is only set while open, so the UA's dialog:not([open]) { display: none } still applies */
	.sideswipe-drawer[open] {
		display: flex;
		transform: translateX(0);
		box-shadow: 25px 0 60px rgba(0, 0, 0, 0.25);
	}

	.sideswipe-drawer::backdrop {
		background: rgba(15, 17, 23, 0.48);
		backdrop-filter: blur(8px);
		-webkit-backdrop-filter: blur(8px);
		opacity: 0;
		transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1),
		            overlay 0.4s allow-discrete,
		            display 0.4s allow-discrete;
	}

	.sideswipe-drawer[open]::backdrop {
		opacity: 1;
	}

	/* Entry animation start points (the dialog goes from display:none to flex) */
	@starting-style {
		.sideswipe-drawer[open] {
			transform: translateX(-100%);
		}

		.sideswipe-drawer[open]::backdrop {
			opacity: 0;
		}

		.sideswipe-drawer[open] .drawer-logo {
			transform: translateX(-14px) scale(0.92);
			opacity: 0;
		}

		.sideswipe-drawer[open] .drawer-ig-cta {
			transform: translateY(22px) scale(0.9);
			opacity: 0;
		}
	}

	.drawer-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 1.25rem 1.5rem;
		border-bottom: 1px solid var(--border-subtle);
	}

	/* Drawer Logo with spring reveal animation */
	.drawer-logo {
		display: flex;
		align-items: center;
		text-decoration: none;
		user-select: none;
		cursor: pointer;
		transform: translateX(-14px) scale(0.92);
		opacity: 0;
		transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) 0.08s, 
		            opacity 0.3s ease 0.08s;
		will-change: transform, opacity;
	}

	.sideswipe-drawer[open] .drawer-logo {
		transform: translateX(0) scale(1);
		opacity: 1;
	}

	.drawer-logo:hover {
		transform: translateY(-2px) scale(1.04);
	}

	.drawer-logo:active {
		transform: translateY(1.5px) scale(0.92);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	.drawer-close-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		background: transparent;
		border: 1px solid var(--border-subtle);
		border-radius: 50%;
		width: 38px;
		height: 38px;
		color: var(--text-main);
		cursor: pointer;
		user-select: none;
		transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), 
		            background-color 0.2s ease, 
		            color 0.2s ease, 
		            border-color 0.2s ease;
		will-change: transform;
	}

	.drawer-close-btn:hover {
		background: var(--accent-navy);
		color: #ffffff;
		border-color: var(--accent-navy);
		transform: scale(1.08) rotate(90deg);
	}

	.drawer-close-btn:active {
		transform: scale(0.88) rotate(90deg);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1);
	}

	.drawer-body {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding: 2rem 1.5rem 2.5rem;
		overflow-y: auto;
	}

	.drawer-nav {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.drawer-nav-item {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.95rem 1rem;
		border-radius: var(--radius-card-sm);
		text-decoration: none;
		color: var(--text-main);
		font-weight: 700;
		font-size: 1.05rem;
		letter-spacing: 0.04em;
		user-select: none;
		transition: background-color 0.2s ease, 
		            color 0.2s ease, 
		            transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
		border-bottom: 1px solid var(--border-subtle);
		will-change: transform;
	}

	.drawer-nav-item:hover {
		background: var(--bg-surface);
		color: var(--accent-navy);
		transform: translateX(5px);
	}

	.drawer-nav-item:active {
		transform: translateX(2px) scale(0.97);
		transition-duration: 0.06s;
	}

	.nav-idx {
		font-size: 0.72rem;
		color: var(--accent-navy);
		font-weight: 700;
	}

	.nav-text {
		flex: 1;
	}

	.nav-arrow {
		color: var(--text-muted);
		transition: transform 0.2s ease;
	}

	.drawer-nav-item:hover .nav-arrow {
		transform: translateX(3px);
		color: var(--accent-navy);
	}

	.drawer-footer {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		padding-top: 1.5rem;
		border-top: 1px solid var(--border-subtle);
	}

	.drawer-ig-cta {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 0.65rem;
		padding: 0.85rem 1.25rem;
		border-radius: var(--radius-pill);
		background: var(--accent-navy);
		color: #ffffff;
		text-decoration: none;
		font-size: 0.78rem;
		font-weight: 700;
		letter-spacing: 0.08em;
		user-select: none;
		box-shadow: 0 4px 16px rgba(20, 33, 61, 0.22);
		transform: translateY(22px) scale(0.9);
		opacity: 0;
		transition: transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) 0.14s, 
		            opacity 0.35s ease 0.14s,
		            box-shadow 0.25s ease, 
		            background-color 0.2s ease;
		will-change: transform, opacity;
	}

	.sideswipe-drawer[open] .drawer-ig-cta {
		transform: translateY(0) scale(1);
		opacity: 1;
	}

	.drawer-ig-cta :global(.ig-svg-icon) {
		transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
		flex-shrink: 0;
	}

	.drawer-ig-cta:hover {
		transform: translateY(-2.5px) scale(1.03);
		box-shadow: 0 10px 28px rgba(20, 33, 61, 0.32);
	}

	.drawer-ig-cta:hover :global(.ig-svg-icon) {
		transform: rotate(-12deg) scale(1.22);
	}

	.drawer-ig-cta:active {
		transform: translateY(2px) scale(0.92);
		box-shadow: 0 2px 6px rgba(20, 33, 61, 0.15);
		transition: transform 0.08s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.08s ease;
	}

	.drawer-ig-cta:active :global(.ig-svg-icon) {
		transform: rotate(0deg) scale(0.92);
		transition: transform 0.08s ease;
	}

	.drawer-location {
		font-size: 0.7rem;
		color: var(--text-muted);
		text-align: center;
		letter-spacing: 0.1em;
	}
</style>
