def dist(x1,x2):
    return math.sqrt(np.sum((x1-x2)**2))
def knn(x,y,query_point,k=5):
    vals=[]
    m=x.shape[0]
    for i in range(m):
        for j in range(m):
            d=dist(query_point,x[i])
            vals.append([d,y[i]]) 
            # store distance and label
            
    vals=sorted(vals)
    vals=vals[:k]
    vals=np.array(vals)
    new_vals=np.unique(vals,return_count=True)
    print(new_vals)
    max_freq_index=np.new_vals[1].argmax()
    pred=vals[0][max_freq_index]
    return pred
