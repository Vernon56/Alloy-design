from matminer.featurizers.composition import ElementProperty
from matminer.featurizers.composition.alloy import WenAlloys
from pymatgen.core.composition import Composition

def featurizer(dataset,col_id):
    wen = WenAlloys()
    wen.set_n_jobs(8)
    alloy_feature = wen.featurize_dataframe(dataset, col_id)
    alloy_feature = alloy_feature.drop(['comp','Weight Fraction','Atomic Fraction','Atomic weight mean','Total weight'],axis=1)
    magpie = ElementProperty.from_preset("magpie")
    magpie.set_n_jobs(8)
    atomic_feature = magpie.featurize_dataframe(dataset, col_id)
    cols = list(atomic_feature.columns)
    at_cols = list(filter(lambda x: x.find('mode')<0,cols))
    at_cols.remove('comp')
    atomic_feature = atomic_feature[at_cols]
    ts = dataset.copy()
    m_solubility = []
    r_solubility = []
    df_solubility = []
    for i in range(ts[[col_id]].shape[0]):
        te = pd.DataFrame(ts[[col_id]].iloc[i,0].element_composition.as_dict(),index=[0])
        m_solubility.append(float(te.apply(max_sb,axis=1)))
        r_solubility.append(float(te.apply(room_sb,axis=1)))
        df_solubility.append(float(te.apply(sb_gap,axis=1)))
    other_features = pd.DataFrame({'max_solublity':m_solubility,'room_solubility':r_solubility,
                                   'solubility_df':df_solubility})
    return pd.concat([atomic_feature,alloy_feature,other_features],axis=1)