import threading
import cProfile


class ProfileThread(threading.Thread):
    def run(self):
        profiler = cProfile.Profile()
        try:
            return profiler.runcall(threading.Thread, self)
        finally:
            profiler.dump_stats('myprofile-%d.profile' % (self.ident,))
