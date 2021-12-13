# This is code for a neurofeedback for meditation project

# Imports
import time
import matplotlib.pyplot as plt
import keyboard

from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels
from brainflow.data_filter import DataFilter, WindowFunctions, DetrendOperations


# Set up + connect to the ganglion
def main():
    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()
    params.board_id = 1
    board_id = 1
    params.serial_port = 'COM4'
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    BoardShim.enable_dev_board_logger()

    board = BoardShim(board_id, params)
    board.prepare_session()

    board.start_stream()
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'Your session is starting.')
    time.sleep(5)
    nfft = DataFilter.get_nearest_power_of_two(sampling_rate)
    data = board.get_board_data()

    eeg_channels = BoardShim.get_eeg_channels(board_id)
    eeg_channel = eeg_channels[1]
    DataFilter.detrend(data[eeg_channel], DetrendOperations.LINEAR.value)
    psd = DataFilter.get_psd_welch(data[eeg_channel], nfft, nfft // 2, sampling_rate,
                                   WindowFunctions.BLACKMAN_HARRIS.value)

    # initializing variables
    running = True
    duration = 0

    # creating timers for each frequency
    time_gamma_concentration = 0
    time_beta_normal = 0
    time_alpha_calm_wakefulness = 0
    time_theta_deep_meditation = 0
    time_delta_deep_sleep = 0

    while running:
        # classifying the types of brainwaves
        gamma_concentration = DataFilter.get_band_power(psd, 32.00, 100.00)
        beta_normal = DataFilter.get_band_power(psd, 6.00, 32.00)
        alpha_calm_wakefulness = DataFilter.get_band_power(psd, 3.00, 6.00)
        theta_deep_meditation = DataFilter.get_band_power(psd, 2.00, 3.00)
        delta_deep_sleep = DataFilter.get_band_power(psd, 1.00, 2.00)
        time.sleep(5)

        # instruction
        print("Continue Meditating")
        print("Hold the Spacebar if you would like to stop.")

        # determining time in each wave type
        # creating a dictionary of frequencies
        frequencies = [gamma_concentration, beta_normal, alpha_calm_wakefulness, theta_deep_meditation,
                       delta_deep_sleep]

        # printing the frequencies

        print('Gamma (Concentration):', gamma_concentration)
        print('Beta (Normal): ', beta_normal)
        print('Alpha (Calm Wakefulness): ', alpha_calm_wakefulness)
        print('Theta (Deep Meditation): ', theta_deep_meditation)
        print('Delta (Deep Sleep):', delta_deep_sleep)

        # counting the time in each wave
        if max(frequencies) == gamma_concentration:
            time_gamma_concentration += 5
            duration += 5

        elif max(frequencies) == beta_normal:
            time_beta_normal += 5
            duration += 5

        elif max(frequencies) == alpha_calm_wakefulness:
            time_alpha_calm_wakefulness += 5
            duration += 5

        elif max(frequencies) == theta_deep_meditation:
            time_theta_deep_meditation += 5
            duration += 5

        elif max(frequencies) == delta_deep_sleep:
            time_delta_deep_sleep += 5
            duration += 5

        # stopping the program
        if keyboard.is_pressed('space'):
            print('Session Complete. You may view your results here.')
            break

    # the meditation session is complete
    # analyzing the meditation session -> creating a graph based on how long in each session

    # dictionary of time values
    time_seconds = [time_gamma_concentration, time_beta_normal, time_alpha_calm_wakefulness, time_theta_deep_meditation,
                    time_delta_deep_sleep]

    # calculating the minutes in each state
    state_minutes = []

    for i in time_seconds:
        i /= 60
        state_minutes.append(i)

    # calculating the percent in each state

    final_percentage = []

    for seconds in time_seconds:
        seconds /= duration
        seconds *= 100
        final_percentage.append(seconds)

    minutes_duration = duration/60

    # Session Summary
    print("Your session was", minutes_duration, "minutes long. You spent", state_minutes[0],
          "minutes in concentration,", state_minutes[1], "minutes in a normal state, ", state_minutes[2],
          "minutes in calm & wakeful state,", state_minutes[3], "minutes in deep meditation, and",
          state_minutes[4], " minutes in deep sleep.")

    print('Gamma (Concentration):', final_percentage[0], "%")
    print('Beta (Normal): ', final_percentage[1], "%")
    print('Alpha (Calm Wakefulness): ', final_percentage[2], "%")
    print('Theta (Deep Meditation): ', final_percentage[3], "%")
    print('Delta (Deep Sleep):', final_percentage[4], "%")

    # creating the x-axis label
    x_values = ['Gamma (Concentration)', 'Beta (Normal)', 'Alpha (Calm Wakefulness', 'Theta (Deep Meditation)',
                'Delta (Deep Sleep)']

    # plotting the final graph
    plt.bar(x_values, state_minutes)
    plt.title('Session Summary')
    plt.xlabel('State of Mind (based on frequency)')
    plt.ylabel('Duration in each Session (mins)')
    plt.show()


# Stopping the program
if __name__ == "__main__":
    main()
