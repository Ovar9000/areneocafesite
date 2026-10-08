export interface MenuItem {
	name: string;
	/** What's in the glass, e.g. "Orange + Espresso" */
	notes?: string;
	/** Philippine pesos */
	price: number;
}

export interface MenuSection {
	id: string;
	title: string;
	/** Small line under the title on the printed menu */
	subtitle?: string;
	items: MenuItem[];
}

/**
 * Single source of truth for the menu, transcribed from the official board
 * (design-assets/LOGOS/119.png). Feeds both the Menu section and the schema.org data.
 */
export const MENU: readonly MenuSection[] = [
	{
		id: 'originals',
		title: 'The Originals',
		subtitle: 'Served iced or hot',
		items: [
			{ name: 'Americano', price: 99 },
			{ name: 'Cafe Latte', price: 119 },
			{ name: 'Hazelnut Latte', price: 119 },
			{ name: 'Caramel Macchiato', price: 119 },
			{ name: 'Spanish Latte', price: 119 },
			{ name: 'White Mocha', price: 119 },
			{ name: 'Butterscotch', price: 119 }
		]
	},
	{
		id: 'house-mix',
		title: 'House Mix',
		subtitle: 'Served iced only',
		items: [
			{ name: 'Sunset Drive', notes: 'Orange + Espresso', price: 149 },
			{ name: 'Acid House', notes: 'Honey + Lemon + Espresso', price: 149 },
			{ name: 'Sweet Static', notes: 'Himalayan Salt + Caramel + Espresso', price: 149 }
		]
	},
	{
		id: 'soft-grooves',
		title: 'Soft Grooves',
		subtitle: 'Milk series',
		items: [
			{ name: 'Purple Haze', notes: 'Taro + Milk', price: 139 },
			{ name: 'Strawberry Fields', notes: 'Strawberry Jam + Milk', price: 139 },
			{ name: 'Sweet Replay', notes: 'Cocoa + Milk', price: 139 }
		]
	},
	{
		id: 'b-sides',
		title: 'B-Sides',
		subtitle: 'Soda pop',
		items: [
			{ name: 'Peach House', notes: 'Honey Peach + Soda', price: 99 },
			{ name: 'Apple FM', notes: 'Green Apple + Soda', price: 99 },
			{ name: 'Day Dream', notes: 'Lychee + Soda', price: 99 }
		]
	}
];

export const ADD_ONS: readonly MenuItem[] = [
	{ name: 'Espresso', price: 50 },
	{ name: 'Oat Milk', price: 40 },
	{ name: 'Flavor', price: 20 }
];
