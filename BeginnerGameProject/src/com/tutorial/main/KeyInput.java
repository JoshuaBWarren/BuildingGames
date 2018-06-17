package com.tutorial.main;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

/*
 * Keyboard input class
 */
public class KeyInput extends KeyAdapter{
	
	private Handler handler;
	
	public KeyInput(Handler handler) { 
	this.handler = handler;
	

	}

	public void keyPressed(KeyEvent e) {
		/*
		 * int key set to letter-binding
		 */
		int key = e.getKeyCode();
		
		/*
		 * For-loop just in case the game has more
		 * than one player.
		 */
		for(int i = 0; i < handler.object.size(); i++) {
			GameObject tempObject = handler.object.get(i);
			
			if(tempObject.getId() == ID.Player) {
				
				if(key == KeyEvent.VK_W) {
					tempObject.setVelY(-5);
				}
				if(key == KeyEvent.VK_S) {
					tempObject.setVelY(5);
				}
				if(key == KeyEvent.VK_D) {
					tempObject.setVelX(5);
				}
				if(key == KeyEvent.VK_A) {
					tempObject.setVelX(-5);
				}
			}
		}
		
		// hit ESC key to exit game
		if(key == KeyEvent.VK_ESCAPE) {
			System.exit(1);
		}
		
	}
	
	public void keyReleased(KeyEvent e) {
		
		int key = e.getKeyCode();
		
		for(int i = 0; i < handler.object.size(); i++) {
			GameObject tempObject = handler.object.get(i);
			
			if(tempObject.getId() == ID.Player) {
				
				if(key == KeyEvent.VK_W) {
					tempObject.setVelY(0);
				}
				if(key == KeyEvent.VK_S) {
					tempObject.setVelY(0);
				}
				if(key == KeyEvent.VK_D) {
					tempObject.setVelX(0);
				}
				if(key == KeyEvent.VK_A) {
					tempObject.setVelX(0);
				}
			}
		}
	}
	
}
