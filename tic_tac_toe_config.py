class TicTacToeConfig():
    # # env config
    # render_train     = False
    # render_test      = False
    # overwrite_render = True
    # record           = False
    # high             = 255.

    # model and training config
    support_size = 10
    action_size = 9
    representation_size   = 18
    hidden_size       = 9
    #These two are defined since value/reward are technically of 2*support_size + 1
    reward_size = 1
    value_size = 1
    # log_freq          = 50
    # eval_freq         = 3000
    # soft_epsilon      = 0

    # # hyper params
    # nsteps_train       = 30000
    batch_size         = 1
    # buffer_size        = 1000
    # target_update_freq = 500
    # gamma              = 0.99
    # learning_freq      = 4
    # state_history      = 4
    # lr_begin           = 0.1
    # lr_end             = lr_begin
    # lr_nsteps          = nsteps_train/2
    # eps_begin          = 1
    # eps_end            = 0.01
    # eps_nsteps         = nsteps_train/2
    # learning_start     = 200
