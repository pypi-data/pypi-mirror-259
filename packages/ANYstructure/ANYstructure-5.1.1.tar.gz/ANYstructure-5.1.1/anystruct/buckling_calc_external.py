from api import CylStru
import pandas as pd

def get_stresses(file = 'C:\DNV\RTHfisk\stress_results.txt'):
    pd_data = pd.read_csv(file,header=0, sep=r'\t', engine='python', na_values = 'N/A')
    pd_data.columns = [val.strip() for val in pd_data.columns.values]
    # for val in pd_data.iterrows():
    #     print(val[1])
    #     quit()
    return pd_data


def calc_buckling(stresses):
    res_list = list()
    for val in stresses.iterrows():

        my_cyl = CylStru(calculation_domain='Unstiffened panel')
        my_cyl.set_stresses(sasd=val[1].SIGMX/1e6, tQsd=abs(val[1].TAUMXY)/1e6, shsd=val[1].SIGMY/1e6)
        my_cyl.set_material(mat_yield=355, emodule=210000, material_factor=1, poisson=0.3)
        my_cyl.set_imperfection()
        my_cyl.set_fabrication_method()
        my_cyl.set_end_cap_pressure_included_in_stress(is_included=True)
        my_cyl.set_uls_or_als(kind='ALS')
        #my_cyl.set_exclude_ring_stiffener()
        #my_cyl.set_length_between_girder(val=8000)
        my_cyl.set_panel_spacing(val=3140)
        my_cyl.set_shell_geometry(radius=1000,thickness=1000*val[1].Thickness, tot_length_of_shell=8500,
                                  distance_between_rings=8500)
        #my_cyl.set_longitudinal_stiffener(hw=260, tw=23, bf=49, tf=28, spacing=680)
        #my_cyl.set_ring_girder(hw=500, tw=15, bf=200, tf=25, stf_type='T', spacing=700)
        my_cyl.set_shell_buckling_parmeters()
        results = my_cyl.get_buckling_results()
        res_list.append((val[1].Case, val[1]['X-coord'], val[1]['Y-coord'], val[1]['Z-coord'],
                         val[1].Thickness, val[1].SIGMX, val[1].SIGMY, val[1].TAUMXY, val[1].Element,
                         results['Unstiffened shell']))

    final_pd = pd.DataFrame(res_list, columns=['Load case', 'x', 'y', 'z', 'thk', 'sigx', 'sigy', 'tauxy',
                                               'Element', 'UF'])
    final_pd.to_csv(r'C:\DNV\RTHfisk\buckling_res.csv')

def read_generated_csv(file = r'C:\DNV\RTHfisk\|.csv'):
    data = pd.read_csv(file, index_col=0)
    return data
if __name__ == '__main__':
    #stresses = read_generated_csv()
    stresses = get_stresses()
    buckling = calc_buckling(stresses=stresses)