import numpy as np

def calculate(list):

    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    np_list = np.array(list).reshape(3, 3)
    calculations = {
      'mean': [[np.mean(np_list[:, i]) for i in range(3)], [np.mean(np_list[i, :]) for i in range(3)], np.mean(list)],
      'variance': [[np.var(np_list[:, i]) for i in range(3)], [np.var(np_list[i, :]) for i in range(3)], np.var(list)],
      'standard deviation': [[np.std(np_list[:, i]) for i in range(3)], [np.std(np_list[i, :]) for i in range(3)], np.std(list)],
      'max': [[np.max(np_list[:, i]) for i in range(3)], [np.max(np_list[i, :]) for i in range(3)], np.max(list)],
      'min': [[np.min(np_list[:, i]) for i in range(3)], [np.min(np_list[i, :]) for i in range(3)], np.min(list)],
      'sum': [[np.sum(np_list[:, i]) for i in range(3)], [np.sum(np_list[i, :]) for i in range(3)], np.sum(list)]
    }


    return calculations