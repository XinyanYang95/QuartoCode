import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
import matplotlib.animation as animation

from shiny import App, render, ui
from faicons import icon_svg

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_numeric("damp_rat", "Damping Ratio (%)", 5.0, min=0.0, max=100.0),
            ui.input_numeric("w", "Frequency (rad/s)", 10.0),
            ui.input_numeric("q0", "Initial Displacement (m)", 0.01),
            ui.input_numeric("q0dot", "Initial Velocity (m/s)", 0.0),
            
        ),
        ui.panel_main(
            ui.output_plot("p"),
        ),
    ),
    ui.div(
        ui.input_action_button(
            "run", "Run simulation", icon=icon_svg("play"), class_="btn-primary"
        )
    ),
)

def server(input, output, session):
    @output
    @render.plot
    def p():
        w=input.w()
        damp_rat=input.damp_rat()
        q0=input.q0()
        q0dot=input.q0dot()

        fig = plt.figure(figsize=(6, 4))
        gs = gridspec.GridSpec(1, 1)
        ax = plt.subplot(gs[0])

        ax.set_xlim(-0, 10)
        ax.set_xlabel(r'$\tau$')
        ax.set_ylabel('q(t)')

        if input.run() > 0:
            damp_rat = float(damp_rat/100.0)
            damped_freq = w*np.sqrt(1-damp_rat**2) #damped frequency, in rad/sec

            cycle = 10.0 #normalized time
            # tao = np.arange(0,cycle + 0.01,0.01) #normalized time
            tao = np.arange(0.0, cycle + 0.02,0.02) #normalized time

            cons = damp_rat / np.sqrt(1-(damp_rat)**2)

            Resp = np.zeros(len(tao))
            zero_line = np.zeros(len(tao))
            count = 0
            amplitude=float((np.sqrt(q0**2 + (2*damp_rat*q0*q0dot/w)+(q0dot/w)**2)) / np.sqrt(1-(damp_rat)**2))
            upper_boundary = np.zeros(len(tao))
            lower_boundary = np.zeros(len(tao))
            for i in tao:
                Resp[count] = (np.exp(-cons * 2*np.pi * i)* (q0*np.cos(2*np.pi * i)+ ((q0dot + damp_rat * w * q0) / damped_freq) * np.sin(2*np.pi * i)))
                upper_boundary[count]=amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
                lower_boundary[count]=-amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
                count += 1

            ax.plot(tao, zero_line, linewidth=0.5, color='black')
            ax.plot(tao, lower_boundary, '--', color='black')
            ax.plot(tao, upper_boundary, '--', color='black')
            resgraph, = ax.plot([], [], color='crimson')

            def response(i):
                resgraph.set_data(tao[0:i], Resp[0:i])
                # dot.set_data(tao[i], Resp[i])
                # return resgraph, dot,
                return resgraph,
    
            anim = animation.FuncAnimation(fig, response, frames=len(tao), interval=20, blit=True)

            return anim
        
        else:
            return fig


def server(input, output, session):
    @output
    @render.plot
    def p():
        w=input.w()
        damp_rat=input.damp_rat()
        q0=input.q0()
        q0dot=input.q0dot()

        fig = plt.figure(figsize=(6, 4))
        gs = gridspec.GridSpec(1, 1)
        ax = plt.subplot(gs[0])

        ax.set_xlim(-0, 10)
        ax.set_xlabel(r'$\tau$')
        ax.set_ylabel('q(t)')

        if input.run() > 0:
            damp_rat = float(damp_rat/100.0)
            damped_freq = w*np.sqrt(1-damp_rat**2) #damped frequency, in rad/sec

            cycle = 10.0 #normalized time
            # tao = np.arange(0,cycle + 0.01,0.01) #normalized time
            tao = np.arange(0.0, cycle + 0.02,0.02) #normalized time

            cons = damp_rat / np.sqrt(1-(damp_rat)**2)

            Resp = np.zeros(len(tao))
            zero_line = np.zeros(len(tao))
            count = 0
            amplitude=float((np.sqrt(q0**2 + (2*damp_rat*q0*q0dot/w)+(q0dot/w)**2)) / np.sqrt(1-(damp_rat)**2))
            upper_boundary = np.zeros(len(tao))
            lower_boundary = np.zeros(len(tao))
            for i in tao:
                Resp[count] = (np.exp(-cons * 2*np.pi * i)* (q0*np.cos(2*np.pi * i)+ ((q0dot + damp_rat * w * q0) / damped_freq) * np.sin(2*np.pi * i)))
                upper_boundary[count]=amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
                lower_boundary[count]=-amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
                count += 1

            ax.plot(tao, zero_line, linewidth=0.5, color='black')
            ax.plot(tao, lower_boundary, '--', color='black')
            ax.plot(tao, upper_boundary, '--', color='black')
            ax.plot(tao, Resp, linewidth=1.0, color='crimson')

        return fig

app = App(app_ui, server)


# def server(input, output, session):
#     @output
#     @render.plot
#     def p():
#         w=input.w()
#         damp_rat=input.damp_rat()
#         q0=input.q0()
#         q0dot=input.q0dot()

#         fig = plt.figure(figsize=(6, 4))
#         gs = gridspec.GridSpec(1, 1)
#         ax = plt.subplot(gs[0])

#         ax.set_xlim(-0, 10)
#         ax.set_xlabel(r'$\tau$')
#         ax.set_ylabel('q(t)')

#         if input.run() > 0:
#             damp_rat = float(damp_rat/100.0)
#             damped_freq = w*np.sqrt(1-damp_rat**2) #damped frequency, in rad/sec

#             cycle = 10.0 #normalized time
#             # tao = np.arange(0,cycle + 0.01,0.01) #normalized time
#             tao = np.arange(0.0, cycle + 0.02,0.02) #normalized time

#             cons = damp_rat / np.sqrt(1-(damp_rat)**2)

#             Resp = np.zeros(len(tao))
#             zero_line = np.zeros(len(tao))
#             count = 0
#             amplitude=float((np.sqrt(q0**2 + (2*damp_rat*q0*q0dot/w)+(q0dot/w)**2)) / np.sqrt(1-(damp_rat)**2))
#             upper_boundary = np.zeros(len(tao))
#             lower_boundary = np.zeros(len(tao))
#             for i in tao:
#                 Resp[count] = (np.exp(-cons * 2*np.pi * i)* (q0*np.cos(2*np.pi * i)+ ((q0dot + damp_rat * w * q0) / damped_freq) * np.sin(2*np.pi * i)))
#                 upper_boundary[count]=amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
#                 lower_boundary[count]=-amplitude * np.exp(-damp_rat*2*np.pi*i/np.sqrt(1-damp_rat**2))
#                 count += 1

#             for i in np.arange(len(tao))[::5]:

#                 ax.clear()
#                 plt.xlabel(r'$\tau$')
#                 plt.ylabel('q(t)')

#                 plt.plot(tao[0:i], Resp[0:i], color='crimson')
#                 plt.plot(tao, zero_line, linewidth=0.5, color='black')
#                 plt.plot(tao, lower_boundary, '--', color='black')
#                 plt.plot(tao, upper_boundary, '--', color='black')
#                 plt.pause(0.0001)

#         return fig

# app = App(app_ui, server)
