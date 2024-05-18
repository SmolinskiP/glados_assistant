from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame # type: ignore
import win32api # type: ignore
import win32con # type: ignore
import win32gui # type: ignore
import os
import pyaudio # type: ignore
import audioop
import threading
import sys

class Animation:
    """Some audio capture specific shit"""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1280
    RECORD_SECONDS = 0.08
    red = 255
    blue = 0
    audio = pyaudio.PyAudio()
    mic_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    @classmethod
    def get_sound_volume(cls):
        """Get normalized sound volume from the microphone."""
        data = cls.mic_stream.read(cls.CHUNK, exception_on_overflow=False)
        rms = audioop.rms(data, 2)
        normalized_value = rms / 5000
        #print("NORMALIZED VALUE: %s" % normalized_value)  # Debugging output
        lower_bound = 4
        upper_bound = 25
        scaled_value = (upper_bound - lower_bound) * normalized_value + lower_bound
        return int(max(lower_bound, min(upper_bound, scaled_value)))

    def __init__(self):
        """Init images and other variables and save them in dictionary"""
        self.void_imgs = [f"img\\frame_{'0' + str(i) if i < 10 else i}_delay-0.03s.gif" for i in range(63)]
        self.current_frame = 0
        self.done = False
        self.terminate = 0

    def start_animation(self):
        """Init pygame and set window properties"""
        pygame.init()
        info = pygame.display.Info()
        screen_width, screen_height = info.current_w, info.current_h
        pos_x = screen_width / 2 - 128
        pos_y = screen_height / 8 * 6
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
        self.screen = pygame.display.set_mode((256, 256), pygame.NOFRAME)
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

        """Start the animation that responds to sound volume."""
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
            shift_factor = self.get_sound_volume()
            #print("SHIFT FACTOR: %s" % shift_factor)  # Debugging output
            self.update_color(shift_factor)

            chosen_img = pygame.image.load(self.void_imgs[self.current_frame]).convert_alpha()
            shift_color = (self.red, 0, self.blue, 255)
            chosen_img.fill(shift_color, special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.fill((255, 0, 128))  # Fuchsia color used for transparency
            self.screen.blit(chosen_img, chosen_img.get_rect(center=self.screen.get_rect().center))
            self.current_frame = (self.current_frame + 1) % len(self.void_imgs)
            pygame.display.flip()
            if self.terminate != 0:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

    def run(self):
        t1 = threading.Thread(target=self.start_animation)
        t1.start()

    def update_color(self, shift_factor):
        """Update the color based on sound volume."""
        if shift_factor > 5:
            self.red -= shift_factor
            self.blue += shift_factor
        else:
            if self.red != 255:
                self.red += 5
            if self.blue != 0:
                self.blue -= 5
        if self.red > 255:
            self.red = 255
        if self.red < 0:
            self.red = 0
        if self.blue > 255:
            self.blue = 255
        if self.blue < 0:
            self.blue = 0
