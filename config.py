class Config(object):

    # SECRET_KEY
    SECRET_KEY = 'A-VERY-LONG-SECRET-KEY'

    # # RECAPTCHA_PUBLIC_KEY
    # RECAPTCHA_PUBLIC_KEY = 'A-VERY-LONG-RECAPTCHA-PUBLIC-KEY'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + "E:/Moses/College_Life/Year3_2/Software_Development_Workshop_III/Code/practice2/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
