import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# <1>
# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0) # also tf.float32 implicitly 암묵적으로 내포
# node3 = tf.add(node1, node2) # node3 = node1 + node2 가능
#
# print("node1: ", node1, "node2: ", node2)
# print("node3: ", node3)

# v1.0
# sess = tf.Session()
# print("sess.run(node1, node2): ", sess.run([node1, node2]))
# print("sess.run(node3): ", sess.run(node3))

# print(tf.__version__)
# tf.print("sess.run(node1, node2): ", [node1, node2])
# tf.print("sess.run(node3): ", node3)
# </1>


# <2>
# v1.0
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)

# v2.0
# a = tf.Variable(name="a")
# adder_node = a + b # + provides a shortcut for tf.add(a, b)

# tf.print(adder_node, feed_dict={a: 3, b: 4.5})
# tf.print(adder_node, feed_dict={a: [1, 3], b: [2, 4]})

# W = tf.Variable(tf.ones(shape=(2,2)), name="W")
# b = tf.Variable(tf.zeros(shape=(2)), name="b")
#
# @tf.function
# def forward(x):
#   return W * x + b
#
# out_a = forward([1,0])
# print(out_a)
# </2>

x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random.normal([1]), name='weight')
b = tf.Variable(tf.random.normal([1]), name='bias')

hypothesis = x_train * W + b
cost = tf.reduce_mean(tf.square(hypothesis - y_train))