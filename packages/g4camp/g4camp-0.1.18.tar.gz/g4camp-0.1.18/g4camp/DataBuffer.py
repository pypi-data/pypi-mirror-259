import numpy as np

class DataBuffer():

  def __init__(self):
    self.particles_per_bunch = 10000
    self.particle_bunches = 1
    self.particle_num = 0
#    self.data_type_particles = np.dtype([('uid',int),('generation',int),('pdgid',int),('x_m',float),('y_m',float),('z_m',float),('time_ns',float),
#                                ('momentum_x_GeV',float),('momentum_y_GeV',float),('momentum_z_GeV',float),('E_tot_GeV',float)])
    self.particles = np.zeros((self.particles_per_bunch, 11), dtype=float)
    # 'particle' row: gen, pdgid, x[m], y[m], z[m], t[ns], Px[GeV], Py[GeV], Pz[GeV], Etot[GeV]
    #
    self.track_points_per_bunch = 100000
    self.track_point_bunches = 1
    self.point_num = 0
#    self.data_type_tracks = np.dtype([('uid',int),('generation',int),('parent_uid',int),('pdgid',int),('x_m',float),('y_m',float),('z_m',float),
#                             ('time_ns',float),('E_tot_GeV',float),('step_length',float)])
    self.tracks = np.zeros((self.track_points_per_bunch, 10), dtype=float) 
    # 'track' row:  uid, gen, pdgid, x[m], y[m], z[m], t[ns], Etot[GeV]
    self.photons = []
    self.status = 'empty' # 'empty' -> 'in_progress' -> 'ready'

  def AddParticle(self, uid, parent_uid, pdgid, x, y, z, t, Px, Py, Pz, Etot):
    self.status = 'in_progress'
    if parent_uid == 0:
        gen = 0
    else:
        gen = 1 + self.GetTrackByUID(parent_uid)[0,1]
    self.particles[self.particle_num] = [uid, gen, pdgid, x, y, z, t, Px, Py, Pz, Etot]
    self.particle_num += 1
    if self.particle_num % self.particles_per_bunch == 0:
      self.particles = np.concatenate((self.particles, np.zeros((self.particles_per_bunch, 11), dtype=int)))
      self.particle_bunches += 1

  def AddPhoton(self, photon):
    self.status = 'in_progress'
    self.photons.append(photon)

  def AddTrackPoint(self, uid, parent_uid, pdgid, x, y, z, t, Etot, l):
    self.status = 'in_progress'
    if parent_uid == 0:
        gen = 0
    else:
        gen = 1 + self.GetTrackByUID(parent_uid)[0,1]
    self.tracks[self.point_num] = [uid, gen, parent_uid, pdgid, x, y, z, t, Etot, l]
    self.point_num += 1
    if self.point_num % self.track_points_per_bunch == 0:
      self.tracks = np.concatenate((self.tracks, np.zeros((self.track_points_per_bunch, 10), dtype=int)))
      self.track_point_bunches += 1
      
  def GetTrackByUID(self, uid):
    return self.tracks[self.tracks[:,0]==uid]

  def CutEmptyItems(self):
    self.tracks = self.tracks[:self.point_num]
    self.particles = self.particles[:self.particle_num]

  def SortItems(self):
    self.tracks = self.tracks[np.lexsort((self.tracks[:,7], self.tracks[:,0]))] # by uid and time

  def Clear(self):
    self.__init__()

  def Close(self):
    self.status = 'ready'

  def IsEmpty(self):
    return self.status == 'empty'

  def IsReady(self):
    return self.status == 'ready'

