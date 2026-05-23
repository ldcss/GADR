# 4. Using React Context

Date: 2019-07-01

## Status

Accepted

## Context

There was a lot of prop-drilling in the component tree.

### Old Render Tree -- A lot of prop-drilling

```
<App/>
  <BananaTabs />
    <MainView /> (✅session, ❌sessionMutator, ❌windowMutator, ❌tabMutator, ✅browserController)
      <Title />
      <WindowListView />          (✅windows, ✅sessionMutator, ❌windowMutator, ❌tabMutator)
        <WindowView />            (✅window, ❌windowMutator, ❌tabMutator)
          <WindowHeader />        (️️⚠️window️, ✅windowMutator, ❌tabMutator)
            <DisclosureButton />  (✅window, ✅windowMutator)
            <VisibilityIcon />    (✅window, ✅windowMutator, ✅tabMutator)
            <WindowTitle />       (✅window, ✅windowMutator)
          <TabList />             (✅window, ❌tabMutator)
            <TabView />           (✅window, ✅tab, ✅tabMutator)
              <TabToolsView />
      <MainViewCmdButtons /> (none)

Legend:
✅prop: actually used by component
⚠️prop: only reading id (e.g. window.id, tab.id)
❌prop: only passing it down to children

```

## Decision

I'm going to try to use React Context with the `useContext` hook to see if I can reduce or eliminate prop-drilling.

## Consequences

### New Render Tree -- No prop-drilling

```
<App/>
  <BananaTabs />
    <MainView /> (✅session, ✅browserController)
      <Title />
      <WindowListView />          (✅windows, ⚛️sessionMutator)
        <WindowView />            (✅window)
          <WindowHeader />        (️️⚠️window️, ⚛️windowMutator)
            <DisclosureButton />  (✅window, ⚛️windowMutator)
            <VisibilityIcon />    (✅window, ⚛️windowMutator, ⚛️tabMutator)
            <WindowTitle />       (✅window, ⚛️windowMutator)
          <TabList />             (✅window)
            <TabView />           (✅window, ✅tab, ⚛️tabMutator)
              <TabToolsView />
      <MainViewCmdButtons /> (none)

Legend:
✅prop: used by component
⚠️prop: only reading id (e.g. window.id, tab.id)
❌prop: only passing it down to children
⚛️context: using context hook
```
