


def get_annual_prob_single(fname, mag, root_):
    """ Get annual probability of exceeding a magnitude of m for the given source
    for a truncated Gutenberg-Richter MFD """
    source = openquake.hazardlib.nrml.to_python(f"{root_}/{fname}")[0][0]
    if type(source.mfd) == openquake.hazardlib.mfd.truncated_gr.TruncatedGRMFD:
        a_val = source.mfd.a_val
        b_val = source.mfd.b_val
        max_mag = source.mfd.max_mag
        annual_prob = 10 ** (a_val - b_val * mag) - 10 ** (a_val - b_val * max_mag)
        return max(annual_prob, 0)
    else:
        rates_tup = source.mfd.get_annual_occurrence_rates()
        magnitudes = [rate[0] for rate in rates_tup]
        rates = [rate[1] for rate in rates_tup]
        func = interp1d(magnitudes, rates)
        return func(mag)


# TRCF002
root = 'fsm/pazarcik/source/fsm_v09'
source_fnames = os.listdir(root)

for source_name in source_fnames:
    source = openquake.hazardlib.nrml.to_python(f"{root}/{source_name}")[0][0]
    if type(source.mfd) == openquake.hazardlib.mfd.truncated_gr.TruncatedGRMFD:
        mmax = source.mfd.max_mag
    else:
        mmax = source.mfd.get_min_max_mag()[1] + 0.05
    print(mmax)
    mags = np.arange(6.7, mmax+0.1, 0.1)
    rps = [get_annual_prob_single(source_name, mag, root) ** -1 for mag in mags]
    axs[0].plot(mags, rps, color='red', lw=0.3, zorder=-10, alpha=0.5)

