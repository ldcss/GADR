## 2. Choosing a React form framework to build Submission Wizard/ Reviewer forms

Date: 2019-01-30

### Status

Accepted

### Context

Previously as part of the xpub project we used `Formik` as our form framework of choice. This relied on using Wrapper components and HOC's for form/ input control. Between then and now React has introduced [Hooks](https://reactjs.org/blog/2019/02/06/react-v16.8.0.html) which many libraries, including `Formik` have implemented to provide easier to use APIs allowing for more readable and concise components. A number of new form frameworks built entirely around hooks have also emerged which we felt we should also consider before settling on a library.

#### formik

https://github.com/libero/reviewer-client/issues/83

Formik seems to have improved a lot since we last worked with it. The introduction of hooks has made implementation simpler and more readable and some of the performance issues we had encountered relating to unnecessary re-renders when using the `Field` component have been fixed.

`Formik` is quite a mature library with its initial release &gt; 3 years ago. The community is very active and there are plenty of resources / examples out there of different use cases.

#### unform

This is a relatively new library first being published 9 months ago. We didn't do to much investigating here as the issues backlog and tagged release dates hint at the community not being widely active and updates not being too frequent (last updated 4 months ago as of writing this).

Unform offers hooks however to register your own form components you need to create your own refs and use `useEffect` to register fields. This makes implementation code more verbose and complicated to follow.

Unform doesn't include any extra dependencies and is quite light weight but this is probably down to it missing some key features which the other libraries do offer (see [RFC](https://github.com/Rocketseat/unform/issues/118))

#### react-hook-form

https://github.com/libero/reviewer-client/issues/84

Designed entirely around hooks and with performance in mind `react-hook-form` uses refs to the DOM elements to maintain form state which makes registering form fields straight forward and is intended to limit any unnecessary re-renders. This may offer us more control over what is rendered in the DOM so we can be more accessibility conscious when developing components.

`react-hook-form` is very light weight and ships with no dependencies. By default it only requires the use of a single `useForm` hook and then can be used with `form` and `input` elements by passing `ref` props. This helps to make form code clean and readable. 

The library is relatively new first published 10 months ago. The community seems responsive and updates are released frequently.

### Decision

We have decided to go with `react-hook-form` based on the following:
- little difference in functionality between `formik` and `react-hook-form` but `react-hook-form` api made code easier to follow and slightly less verbose in most use-cases
- `react-hook-form` has 0 dependencies and a slightly smaller bundle size. 
- seems to have a greater focus on implementation through hooks rather than `Input` components meaning we should find it easier to control what is rendered to the DOM (good for accessibility)