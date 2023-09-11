import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

def PlotVib(damp_rat, w, q0, q0dot):
  '''
  ARGUMENTS: damp_rat, w, q0, q0dot

  damp_rat: damping ratio, in %.
  w: damped frequency, in rad/sec.
  q0: initial displacement, in m.
  q0dot: initial velocity, in m/s.

  RETURN: fig, response, tao

  '''

  plt.rcParams["animation.html"] = "jshtml"
  plt.rcParams['figure.dpi'] = 100  
  plt.rcParams['animation.embed_limit'] = 2**128
  plt.ioff()

  damp_rat = float(damp_rat/100)
  damped_freq = w*np.sqrt(1-damp_rat**2) #damped frequency, in rad/sec

  cycle = 10 #normalized time
  # tao = np.arange(0,cycle + 0.01,0.01) #normalized time
  tao = np.arange(0,cycle + 0.02,0.02) #normalized time

  plt.xlabel(r'$\tau$')
  plt.ylabel('q(t)')
  cons = damp_rat / np.sqrt(1-(damp_rat)**2)

  Resp =np.zeros(len(tao))
  zero_line=np.zeros(len(tao))
  count = 0
  amplitude=float((np.sqrt(q0**2 + (2*damp_rat*q0*q0dot/w)+(q0dot/w)**2)) / np.sqrt(1-(damp_rat)**2))
  upper_boundary=np.zeros(len(tao))
  lower_boundary=np.zeros(len(tao))
  for i in tao:
      Resp[count] = (np.exp(-cons * 2*np.pi * i)* (q0*np.cos(2*np.pi * i)+ ((q0dot + damp_rat * w * q0) / damped_freq) * np.sin(2*np.pi * i)))
      upper_boundary[count]=amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
      lower_boundary[count]=-amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
      count += 1

  fig = plt.figure(figsize=(6, 4))
  gs = gridspec.GridSpec(1, 1) 
  ax = plt.subplot(gs[0])

  ax.set_xlim(-0, 10)
  ax.set_xlabel(r'$\tau$')
  ax.set_ylabel('q(t)')

  ax.plot(tao, zero_line, linewidth=0.5, color='black')
  ax.plot(tao, lower_boundary, '--', color='black')
  ax.plot(tao, upper_boundary, '--', color='black')

  resgraph, = ax.plot([], [], color='crimson')
  # dot, = ax.plot([], [], 'o', color='red')

  def response(i):
      resgraph.set_data(tao[0:i], Resp[0:i])
      # dot.set_data(tao[i], Resp[i])
      # return resgraph, dot,
      return resgraph,

  return fig, response, tao
