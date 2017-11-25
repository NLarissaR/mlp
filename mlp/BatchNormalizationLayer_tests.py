{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NotImplementedError",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNotImplementedError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-3fe96e79dfcc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0mactivation_layer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mgamma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbeta\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mBN_fprop\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mactivation_layer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfprop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_inputs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m BN_bprop = activation_layer.bprop(\n\u001b[1;32m     21\u001b[0m     test_inputs, BN_fprop, test_grads_wrt_outputs)\n",
      "\u001b[0;32m~/workspace/mlpractical/mlp/layers.py\u001b[0m in \u001b[0;36mfprop\u001b[0;34m(self, inputs, stochastic)\u001b[0m\n\u001b[1;32m    359\u001b[0m         \u001b[0;34m\"\"\"Forward propagates inputs through a layer.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    360\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 361\u001b[0;31m         \u001b[0mmu\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    362\u001b[0m         \u001b[0mvar\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvar\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    363\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNotImplementedError\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from mlp.layers import BatchNormalizationLayer\n",
    "test_inputs = np.array([[-1.38066782, -0.94725498, -3.05585424,  2.28644454,  0.85520889,\n",
    "         0.10575624,  0.23618609,  0.84723205,  1.06569909, -2.21704034],\n",
    "       [ 0.11060968, -0.0747448 ,  0.56809029,  2.45926149, -2.28677816,\n",
    "        -0.9964566 ,  2.7356007 ,  1.98002308, -0.39032315,  1.46515481]])\n",
    "test_grads_wrt_outputs = np.array([[-0.43857052,  1.00380109, -1.18425494,  0.00486091,  0.21470207,\n",
    "        -0.12179054, -0.11508482,  0.738482  , -1.17249238,  0.69188295],\n",
    "       [ 1.07802015,  0.69901145,  0.81603688, -1.76743026, -1.24418692,\n",
    "        -0.65729963, -0.50834305, -0.49016145,  1.63749743, -0.71123104]])\n",
    "\n",
    "#produce BatchNorm fprop and bprop\n",
    "activation_layer = BatchNormalizationLayer(input_dim=10)\n",
    "\n",
    "beta = np.array(10*[0.3])\n",
    "gamma = np.array(10*[0.5])\n",
    "\n",
    "activation_layer.params = [gamma, beta]\n",
    "BN_fprop = activation_layer.fprop(test_inputs)\n",
    "BN_bprop = activation_layer.bprop(\n",
    "    test_inputs, BN_fprop, test_grads_wrt_outputs)\n",
    "BN_grads_wrt_params = activation_layer.grads_wrt_params(\n",
    "    test_inputs, test_grads_wrt_outputs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BN_fprop' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-5-feae0953a7c0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m        [ 0.7999955 ,  0.79998686,  0.79999924,  0.7996655 , -0.19999899,\n\u001b[1;32m      4\u001b[0m         -0.19999177,  0.7999984 ,  0.79999221, -0.19999528,  0.79999926]])\n\u001b[0;32m----> 5\u001b[0;31m assert BN_fprop.shape == true_fprop_outputs.shape, (\n\u001b[0m\u001b[1;32m      6\u001b[0m     \u001b[0;34m'Layer bprop returns incorrect shaped array. '\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0;34m'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'BN_fprop' is not defined"
     ]
    }
   ],
   "source": [
    "true_fprop_outputs = np.array([[-0.1999955 , -0.19998686, -0.19999924, -0.1996655 ,  0.79999899,\n",
    "         0.79999177, -0.1999984 , -0.19999221,  0.79999528, -0.19999926],\n",
    "       [ 0.7999955 ,  0.79998686,  0.79999924,  0.7996655 , -0.19999899,\n",
    "        -0.19999177,  0.7999984 ,  0.79999221, -0.19999528,  0.79999926]])\n",
    "assert BN_fprop.shape == true_fprop_outputs.shape, (\n",
    "    'Layer bprop returns incorrect shaped array. '\n",
    "    'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\n",
    "    .format(true_fprop_outputs.shape, BN_fprop.shape)\n",
    ")\n",
    "assert np.allclose(np.round(BN_fprop, decimals=2), np.round(true_fprop_outputs, decimals=2)), (\n",
    "'Layer bprop does not return correct values. '\n",
    "'Correct output is \\n\\n{0}\\n\\n but returned output is \\n\\n{1}\\n\\n difference is \\n\\n{2}'\n",
    ".format(true_fprop_outputs, BN_fprop, BN_fprop-true_fprop_outputs)\n",
    ")\n",
    "\n",
    "print(\"Batch Normalization F-prop test passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BN_bprop' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-fd0ef8943483>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m          \u001b[0;34m-\u001b[0m\u001b[0;36m5.03719464e-07\u001b[0m\u001b[0;34m,\u001b[0m  \u001b[0;34m-\u001b[0m\u001b[0;36m1.69038704e-05\u001b[0m\u001b[0;34m,\u001b[0m   \u001b[0;36m1.82061629e-05\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m          -5.62083224e-07]])\n\u001b[0;32m----> 9\u001b[0;31m assert BN_bprop.shape == true_bprop_outputs.shape, (\n\u001b[0m\u001b[1;32m     10\u001b[0m     \u001b[0;34m'Layer bprop returns incorrect shaped array. '\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0;34m'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'BN_bprop' is not defined"
     ]
    }
   ],
   "source": [
    "true_bprop_outputs = np.array([[ -9.14558020e-06,   9.17665617e-06,  -8.40575535e-07,\n",
    "          6.85384297e-03,   9.40668131e-07,   7.99795574e-06,\n",
    "          5.03719464e-07,   1.69038704e-05,  -1.82061629e-05,\n",
    "          5.62083224e-07],\n",
    "       [  9.14558020e-06,  -9.17665617e-06,   8.40575535e-07,\n",
    "         -6.85384297e-03,  -9.40668131e-07,  -7.99795574e-06,\n",
    "         -5.03719464e-07,  -1.69038704e-05,   1.82061629e-05,\n",
    "         -5.62083224e-07]])\n",
    "assert BN_bprop.shape == true_bprop_outputs.shape, (\n",
    "    'Layer bprop returns incorrect shaped array. '\n",
    "    'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\n",
    "    .format(true_bprop_outputs.shape, BN_bprop.shape)\n",
    ")\n",
    "assert np.allclose(np.round(BN_bprop, decimals=2), np.round(true_bprop_outputs, decimals=2)), (\n",
    "'Layer bprop does not return correct values. '\n",
    "'Correct output is \\n\\n{0}\\n\\n but returned output is \\n\\n{1}\\n\\n difference is \\n\\n{2}'\n",
    ".format(true_bprop_outputs, BN_bprop, BN_bprop-true_bprop_outputs)\n",
    ")\n",
    "\n",
    "print(\"Batch Normalization B-prop test passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BN_grads_wrt_params' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-5b4e558c68e3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mgrads_wrt_gamma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgrads_wrt_beta\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBN_grads_wrt_params\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m true_grads_wrt_gamma = np.array(([ 1.51657703, -0.30478163,  2.00028878, -1.77110552,  1.45888603,\n\u001b[1;32m      3\u001b[0m         0.53550028, -0.39325697, -1.2286243 , -2.8099633 , -1.40311192]))\n\u001b[1;32m      4\u001b[0m true_grads_wrt_beta = np.array([ 0.63944963,  1.70281254, -0.36821806, -1.76256935, -1.02948485,\n\u001b[1;32m      5\u001b[0m        -0.77909018, -0.62342786,  0.24832055,  0.46500505, -0.01934809])\n",
      "\u001b[0;31mNameError\u001b[0m: name 'BN_grads_wrt_params' is not defined"
     ]
    }
   ],
   "source": [
    "grads_wrt_gamma, grads_wrt_beta = BN_grads_wrt_params\n",
    "true_grads_wrt_gamma = np.array(([ 1.51657703, -0.30478163,  2.00028878, -1.77110552,  1.45888603,\n",
    "        0.53550028, -0.39325697, -1.2286243 , -2.8099633 , -1.40311192]))\n",
    "true_grads_wrt_beta = np.array([ 0.63944963,  1.70281254, -0.36821806, -1.76256935, -1.02948485,\n",
    "       -0.77909018, -0.62342786,  0.24832055,  0.46500505, -0.01934809])\n",
    "\n",
    "assert grads_wrt_gamma.shape == true_grads_wrt_gamma.shape, (\n",
    "    'Layer bprop returns incorrect shaped array. '\n",
    "    'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\n",
    "    .format(true_grads_wrt_gamma.shape, grads_wrt_gamma.shape)\n",
    ")\n",
    "assert np.allclose(np.round(grads_wrt_gamma, decimals=2), np.round(true_grads_wrt_gamma, decimals=2)), (\n",
    "'Layer bprop does not return correct values. '\n",
    "'Correct output is \\n\\n{0}\\n\\n but returned output is \\n\\n{1}\\n\\n difference is \\n\\n{2}'\n",
    ".format(true_grads_wrt_gamma, grads_wrt_gamma, grads_wrt_gamma-true_grads_wrt_gamma)\n",
    ")\n",
    "\n",
    "assert grads_wrt_beta.shape == true_grads_wrt_beta.shape, (\n",
    "    'Layer bprop returns incorrect shaped array. '\n",
    "    'Correct shape is \\n\\n{0}\\n\\n but returned shape is \\n\\n{1}.'\n",
    "    .format(true_grads_wrt_beta.shape, grads_wrt_beta.shape)\n",
    ")\n",
    "assert np.allclose(np.round(grads_wrt_beta, decimals=2), np.round(true_grads_wrt_beta, decimals=2)), (\n",
    "'Layer bprop does not return correct values. '\n",
    "'Correct output is \\n\\n{0}\\n\\n but returned output is \\n\\n{1}\\n\\n difference is \\n\\n{2}'\n",
    ".format(true_grads_wrt_beta, grads_wrt_beta, grads_wrt_beta-true_grads_wrt_beta)\n",
    ")\n",
    "\n",
    "print(\"Batch Normalization grads wrt to params test passed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
