package com.tutorial.main;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class BasicEnemy extends GameObject{
	
	private Handler handler;

	public BasicEnemy(int x, int y, ID id, Handler handler) {
		super(x, y, id, handler);
		
		this.handler = handler;
		
		velX = 5;
		velY = 5;
	}
	
	public Rectangle getBounds() {
		return new Rectangle(x, y, 16, 16);
	}

	public void tick() {
		x += velX;
		y += velY;
		
		/*
		 * if it reaches the top/bottom
		 */
		if(y <= 0 || y >= Game.HEIGHT - 32) {
			
			// reverse direction
			velY *= -1;
		}
		
		/*
		 * if it reaches the right/left part of the screen
		 */
		if(x <= 0 || x >= Game.WIDTH - 16) {
			
			// reverse direction
			velX *= -1;
		}
		
		handler.addObject(new Trail(x, y, ID.Trail, Color.red, 16, 16, 0.02f, handler));
		
	}

	public void render(Graphics g) {


		g.setColor(Color.red);g.fillRect(x, y, 16, 16);
		
	}

	
}
