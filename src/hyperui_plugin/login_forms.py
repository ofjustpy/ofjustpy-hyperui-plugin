from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
def SplitWithGraphic(key):
    with writer_ctx:
        with Section(classes='bg-white') as comp_box:
            with Div(classes='lg:grid lg:min-h-screen lg:grid-cols-12'):
                with Aside(classes='relative block h-16 lg:order-last lg:col-span-5 lg:h-full xl:col-span-6'):
                    with Img(alt='Pattern',
                             src='https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', classes='absolute inset-0 h-full w-full object-cover'):
                        pass

                with Main(classes='flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6'):
                    with Div(classes='max-w-xl lg:max-w-3xl'):
                        with A(classes='block text-blue-600',
                               href='/'):
                            with Span(classes='sr-only',
                                      text='Home'):
                                pass
                            with FontAwesomeIcon(label="faHippo", classes="w-5 h-5",):
                                pass

                        with H1(classes='mt-6 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl',
                                text='Welcome to Squid 🦑'):
                            pass

                        with P(classes='mt-4 leading-relaxed text-gray-500', text='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eligendi nam dolorum aliquam, quibusdam aperiam voluptatum.'):
                            pass

                        with Form(key=key,
                                  classes='mt-8 grid grid-cols-6 gap-6', action='#'):
                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='FirstName',
                                           classes='block text-sm font-medium text-gray-700',
                                           text='First Name'):
                                    pass

                                with TextInput(type='text',
                                               key='FirstName',
                                               name='first_name', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='LastName', classes='block text-sm font-medium text-gray-700', text='Last Name'):
                                    pass

                                with TextInput(type='text', key='LastName', name='last_name', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6'):
                                with Label(for_='Email', classes='block text-sm font-medium text-gray-700', text='Email'):
                                    pass

                                with TextInput(type='email', key='Email', name='email', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='Password', classes='block text-sm font-medium text-gray-700', text='Password'):
                                    pass

                                with TextInput(type='password', key='Password', name='password', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='PasswordConfirmation', classes='block text-sm font-medium text-gray-700', text='Password Confirmation'):
                                    pass

                                with TextInput(type='password', key='PasswordConfirmation', name='password_confirmation', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6'):
                                with Label(classes='flex gap-4', for_='MarketingAccept'):
                                    with TextInput(key=f"inp_{key}", type='checkbox',  name='marketing_accept', classes='h-5 w-5 rounded-md border-gray-200 bg-white shadow-sm'):
                                        pass

                                    with Span(classes='text-sm text-gray-700', text='I want to receive emails about events, product updates and company announcements.'):
                                        pass

                            with Div(classes='col-span-6'):
                                with P(classes='text-sm text-gray-500', text='By creating an account, you agree to our '):
                                    with A(href='#', classes='text-gray-700 underline', text='terms and conditions and'):
                                        pass

                                    with A(href='#', classes='text-gray-700 underline', text='privacy policy'):
                                        pass

                            with Div(classes='col-span-6 sm:flex sm:items-center sm:gap-4'):
                                with Button(key=f"btn_{key}", classes='inline-block shrink-0 rounded-md border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-blue-500', text='Create an account'):
                                    pass

                                with P(classes='mt-4 text-sm text-gray-500 sm:mt-0', text='Already have an account? '):
                      
                                    with A(href='#', classes='text-gray-700 underline', text='Log in'):
                                        pass
                                    
    return comp_box


#TODO: argumentize the func; use proper key for TextInputs
# for now copy and inline modify 
def SplitWithContent():
    with writer_ctx:
        with Section(classes='bg-white') as comp_box:
            with Div(classes='lg:grid lg:min-h-screen lg:grid-cols-12'):
                with Section(classes='relative flex h-32 items-end bg-gray-900 lg:col-span-5 lg:h-full xl:col-span-6'):
                    with Img(alt='Night', src='https://images.unsplash.com/photo-1617195737496-bc30194e3a19?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', classes='absolute inset-0 h-full w-full object-cover opacity-80'):
                        pass

                    with Div(classes='hidden lg:relative lg:block lg:p-12'):
                        with A(classes='block text-white', href='/'):
                            with Span(classes='sr-only', text='Home'):
                                pass
                            with FontAwesomeIcon(label="faHippo", classes="w-5 h-5",):
                                pass

                        with H2(classes='mt-6 text-2xl font-bold text-white sm:text-3xl md:text-4xl', text='Welcome to Squid 🦑'):
                            pass

                        with P(classes='mt-4 leading-relaxed text-white/90', text='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eligendi nam dolorum aliquam, quibusdam aperiam voluptatum.'):
                            pass

                with Main(classes='flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6'):
                    with Div(classes='max-w-xl lg:max-w-3xl'):
                        with Div(classes='relative -mt-16 block lg:hidden'):
                            with A(classes='inline-flex h-16 w-16 items-center justify-center rounded-full bg-white text-blue-600 sm:h-20 sm:w-20', href='/'):
                                with Span(classes='sr-only', text='Home'):
                                    pass
                                with FontAwesomeIcon(label="faHippo", classes="w-5 h-5",):
                                    pass

                            with H1(classes='mt-2 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl', text='Welcome to Squid 🦑'):
                                pass

                            with P(classes='mt-4 leading-relaxed text-gray-500', text='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eligendi nam dolorum aliquam, quibusdam aperiam voluptatum.'):
                                pass

                        with Form(key="form", classes='mt-8 grid grid-cols-6 gap-6', action='#'):
                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='FirstName', classes='block text-sm font-medium text-gray-700', text='First Name'):
                                    pass

                                with TextInput(type='text', key='FirstName', name='first_name', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='LastName', classes='block text-sm font-medium text-gray-700', text='Last Name'):
                                    pass

                                with TextInput(type='text', key='LastName', name='last_name', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6'):
                                with Label(for_='Email', classes='block text-sm font-medium text-gray-700', text='Email'):
                                    pass

                                with TextInput(type='email', key='Email', name='email', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='Password', classes='block text-sm font-medium text-gray-700', text='Password'):
                                    pass

                                with TextInput(type='password', key='Password', name='password', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6 sm:col-span-3'):
                                with Label(for_='PasswordConfirmation', classes='block text-sm font-medium text-gray-700', text='Password Confirmation'):
                                    pass

                                with TextInput(type='password', key='PasswordConfirmation', name='password_confirmation', classes='mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'):
                                    pass

                            with Div(classes='col-span-6'):
                                with Label(for_='MarketingAccept', classes='flex gap-4'):
                                    with TextInput(type='checkbox', key='MarketingAccept', name='marketing_accept', classes='h-5 w-5 rounded-md border-gray-200 bg-white shadow-sm'):
                                        pass

                                    with Span(classes='text-sm text-gray-700', text='I want to receive emails about events, product updates and company announcements.'):
                                        pass

                            with Div(classes='col-span-6'):
                                with P(classes='text-sm text-gray-500', text='By creating an account, you agree to our '):
                                    with A(href='#', classes='text-gray-700 underline', text='terms and conditions and'):
                                        pass

                                    with A(href='#', classes='text-gray-700 underline', text='privacy policy'):
                                        pass

                            with Div(classes='col-span-6 sm:flex sm:items-center sm:gap-4'):
                                with Button(key="btn", classes='inline-block shrink-0 rounded-md border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-blue-500', text='Create an account'):
                                    pass

                                with P(classes='mt-4 text-sm text-gray-500 sm:mt-0', text='Already have an account? '):
                                    with A(href='#', classes='text-gray-700 underline', text='Log in'):
                                        pass
    return comp_box
